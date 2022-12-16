import requests
from bs4 import BeautifulSoup
import json

from classes import (
    Element,
    Slot,
    SlotType,
    Manufacture,
    VaultHunter,
    Equipment,
    EquipmentSource,
    BuildLink,
)

"""
This optionally grabs the html files
Then parses the html files and generates JSON files of the results
"""

lootlemon_base_url = 'https://www.lootlemon.com'
lootlemon_db_url = 'https://www.lootlemon.com/db/borderlands-3'
lootlemon_loot_source = 'https://www.lootlemon.com'
save_path = 'html_data'

def get_lootlemon_html(url_extention, path_extention=None):
    if not path_extention:
        path_extention = url_extention
    if not url_extention.startswith('/'):
        url_extention = '/' + url_extention
    resp = requests.get(lootlemon_db_url + url_extention)
    with open(f"{save_path}/lootlemon_{path_extention}.html", 'w') as hf:
        hf.write(resp.text)

def get_lootlemon_weapons():
    resp = requests.get(lootlemon_db_url + '/weapons')
    weapons = resp.text
    with open(f"{save_path}/lootlemon_weapons.html", 'w') as hf:
        hf.write(weapons)

if False:
    """Turn on to get updated html files"""
    get_lootlemon_html('weapons')
    get_lootlemon_html('shields')
    get_lootlemon_html('grenade-mods')
    get_lootlemon_html('class-mods')
    get_lootlemon_html('artifacts')

def process_lootlemon(path_extention, equipment_obj=True):
    """
    Parse the saved html file and return the data as a json object
    """
    with open(f"{save_path}/lootlemon_{path_extention}.html", 'r') as hf:
        bs = BeautifulSoup(hf, 'lxml')
    extention_data = []
    for item in bs.find_all('div', {"role": "listitem"}):
        with open('temp.html', 'w') as tf:
            tf.write(item.prettify())
        data = {}
        db_cell = item.find_all('div', {'class': 'db_cell'})
        if not db_cell:
            continue
        data['name'] = db_cell[0].string
        data['drop_type'] = item.find('img')['title']
        if len(db_cell) == 6:
            """Its equipment"""
            data['equipment_type'] = db_cell[1].string
            data['manufacture'] = db_cell[2].string
            all_elements = item.find_all('img', {'class': "icon-round"})
            elements = [e for e in all_elements if 'w-condition-invisible' not in e['class']]
            data['elements'] = [e['src'].split('_')[-1][:-4] for e in elements]
            data['content'] = db_cell[4].string
            source_index = 5
        elif len(db_cell) == 4:
            if path_extention == 'class-mods':
                data['vault_hunter'] = db_cell[1].string
            elif path_extention == 'artifacts':
                data['artifact_type'] = db_cell[1].string
            data['content'] = db_cell[2].string
            source_index = 3

        if db_cell[source_index].find('div', {'class': 'w-embed'}) is not None:
            data['source'] = {
                'mob': db_cell[source_index].find('div', {'class': 'w-embed'}).text.strip(),
                'location': db_cell[source_index].find('div', {'class': 'embed-over-line'}).text.strip(),
                'link': db_cell[source_index].find('a', {'aria-label': 'source link'})['href'],
            }
        else:
            data['source'] = None
        data['image'] = item.find('img')['src']
        data['extension'] = item.find('a')['href']
        if equipment_obj:
            equipment = generate_equipment_object(item=item, slot_type=path_extention[:-1].replace('-', '_'))
            extention_data.append(equipment)
        else:
            extention_data.append(data)
    return extention_data

def generate_equipment_object(item, slot_type):
    db_cell = item.find_all('div', {'class': 'db_cell'})
    equipment = Equipment()
    equipment.slot = getattr(Slot, slot_type.upper())
    equipment.slot_type = create_slot_obj(db_cell[1].string)
    equipment.elements = create_element_obj_list(item.find_all('img', {'class': "icon-round"}))
    equipment.name = db_cell[0].string
    equipment.source = create_source_data(
        source_string=db_cell[-1],
        source_format_string=item.find('img')['title'],
        content_string=db_cell[2].string,
        image_src=item.find('img')['src'],
        page_url=item.find('a', {'aria-label': 'Page link'})['href'],
    )
    if len(db_cell) == 6:
        equipment.manufactures = create_manufacture(db_cell[2].string.upper())
    return equipment

def create_slot_obj(string):
    string = string.upper().replace(' ', '_')
    if string == 'ASSAULT RIFLE':
        string = 'ASSAULT_RIFLE'
    if string == 'SNIPER':
        string = 'SNIPER_RIFLE'
    if string == 'LAUNCHER':
        string = 'ROCKET_LAUNCHER'
    return getattr(SlotType, string)

def create_element_obj_list(string):
    elements_list = [e for e in string if 'w-condition-invisible' not in e['class']]
    elements_strings = [e['src'].split('_')[-1][:-4] for e in elements_list]
    elements = []
    for element in elements_strings:
        if element == 'Nonelemental':
            element = 'Kenetic'
        if element == 'Incindiary':
            element = 'Fire'
        if element == 'Corrosive':
            element = 'Acid'
        elements.append(getattr(Element, element.upper()))
    return elements

def create_source_data(
    source_string,
    source_format_string,
    content_string,
    image_src,
    page_url,
):
    source = EquipmentSource()
    if source_string.find('div', {'class': 'w-embed'}) is not None:
        source.mob = source_string.find('div', {'class': 'w-embed'}).text.strip()
        source.location = source_string.find('div', {'class': 'embed-over-line'}).text.strip()
        source.location_link = lootlemon_loot_source + source_string.find('a', {'aria-label': 'source link'})['href']
        source.link = lootlemon_base_url + page_url
    source.drop_source_format = source_format_string
    source.content = content_string
    source.image_url = image_src
    return source

def create_manufacture(string):
    string_list = [s.strip() for s in string.split('|')]
    manufactures = []
    for string in string_list:
        manufactures.append(getattr(Manufacture, string))
    return manufactures

def save_json_object(path_extention, data=None):
    if data is None:
        data = process_lootlemon(path_extention=path_extention, equipment_obj=True)

    save_data = []
    for d in data:
        if isinstance(d, Equipment):
            save_data.append(d.put)
        else:
            save_data.append(d)

    with open(f"{save_path}/lootlemon_{path_extention}.json", 'w') as jf:
        jf.write(json.dumps(save_data, indent=4))
    
    # with open(f"{save_path}/lootlemon_{path_extention}.json", 'r') as jf:
    #     data = json.load(jf)
    # for d in data:
    #     Equipment.build(d)
    # a = 1

save_json_object('weapons')
save_json_object('shields')
save_json_object('grenade-mods')
save_json_object('class-mods')
save_json_object('artifacts')

x=1
