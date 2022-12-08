import requests
from bs4 import BeautifulSoup
import json

"""
This optionally grabs the html files
Then parses the html files and generates JSON files of the results
"""

lootlemon_url = 'https://www.lootlemon.com/db/borderlands-3/'
save_path = 'html_data'

def get_lootlemon_html(url_extention, path_extention=None):
    if not path_extention:
        path_extention = url_extention
    resp = requests.get(lootlemon_url + url_extention)
    with open(f"{save_path}/lootlemon_{path_extention}.html", 'w') as hf:
        hf.write(resp.text)

def get_lootlemon_weapons():
    resp = requests.get(lootlemon_url + 'weapons')
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

def process_lootlemon(path_extention):
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
        extention_data.append(data)
    return extention_data

def save_json_object(path_extention, data=None):
    if data is None:
        data = process_lootlemon(path_extention=path_extention)

    with open(f"{save_path}/lootlemon_{path_extention}.json", 'w') as jf:
        jf.write(json.dumps(data, indent=4))

save_json_object('weapons')
save_json_object('shields')
save_json_object('grenade-mods')
save_json_object('class-mods')
save_json_object('artifacts')
