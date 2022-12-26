from pydantic import BaseModel
from typing import List
from enum import Enum
import json
import re
import os
import webbrowser
from datetime import datetime

from phtml import(
    Header,
    Div,
    Paragraph,
    LineBreak,
    Link,
    Style,
)


DATE_STRING = '%Y-%m-%dT%H:%M:%S.%f'


class Element(Enum):
    FIRE = 'fire'
    SHOCK = 'shock'
    ACID = 'acid'
    CRYO = 'cryo'
    RADIATION = 'radiation'
    KENETIC = 'kenetic'


class ElementColor(Enum):
    FIRE = 'red'
    SHOCK = 'blue'
    ACID = 'green'
    CRYO = 'cyan'
    RADIATION = 'yellow'
    KENETIC = 'white'


class Slot(Enum):
    WEAPON = 'weapon'
    ARTIFACT = 'artifact'
    CLASS_MOD = 'class_mod'
    GRENADE_MOD = 'grenade_mod'
    SHIELD = 'shield'
    EMPTY = None


class SlotType(Enum):
    STANDARD = 'standard'
    UNIQUE = 'unique'
    EMPTY = None

    # Weapons
    ASSAULT_RIFLE = 'assault_rifle'
    PISTOL = 'pistol'
    ROCKET_LAUNCHER = 'rocket_launcher'
    SHOTGUN = 'shotgun'
    SMG = 'smg'
    SNIPER_RIFLE = 'sniper_rifle'

    # Shields
    BOOSTER = 'booster'
    REFLECT = 'reflect'
    DAMAGE = 'damage'
    NOVA = 'nova'
    TURTLE = 'turtle'
    AMPLIFY = 'amplify'
    ROID = 'roid'
    SPIKE = 'spike'
    ABSORB = 'absorb'

    # Grenades
    TRANSFUSION = 'transfusion'
    MIRV = 'mirv'
    BOUNCING_BETTY = 'bouncing_betty'
    AREA_OF_EFFECT = 'area_of_effect'
    SINGULARITY = 'singularity'

    # Artifacts
    MELEE = 'melee'
    SLAM = 'slam'
    UNIVERSAL = 'universal'
    SLIDE = 'slide'

    AMARA = 'amara'
    FL4K = 'fl4k'
    MOZE = 'moze'
    ZANE = 'zane'

    WEAPON = 'weapon'
    ARTIFACT = 'artifact'
    CLASS_MOD = 'class_mod'
    GRENADE_MOD = 'grenade_mod'
    SHIELD = 'shield'


class Manufacture(Enum):
    HYPERION = 'hyperion'
    VLADOF = 'vladof'
    COV = 'cov'
    ATLAS = 'atlas'
    TEDIORE = 'tediore'
    DAHL = 'dahl'
    JAKOBS = 'jakobs'
    MALIWAN = 'maliwan'
    TORGUE = 'torgue'
    ERIDIAN = 'eridian'
    ANSHIN = 'anshin'
    PANGOLIN = 'pangolin'
    UNKNOWN = 'unknown'


class VaultHunter(Enum):
    AMARA = 'amara'
    FL4K = 'fl4k'
    MOZE = 'moze'
    ZANE = 'zane'


class VaultHunterColor(Enum):
    AMARA = 'pink'
    FL4K = 'lightgreen'
    MOZE = 'orangered'
    ZANE = 'cyan'


class ChangeLogEntry(BaseModel):
    note: str
    date: datetime = datetime.now()

    @property
    def put(self):
        details = {
            'note': self.note,
            'date': datetime.strftime(self.date, DATE_STRING),
        }
        return details

    @classmethod
    def build(cls, data):
        details = {
            'note': data['note'],
            'date': datetime.strptime(data['date'], DATE_STRING),
        }
        return  cls(**details)


class EquipmentSource(BaseModel):
    drop_source_format: str = None
    content: str = None
    mob: str = None
    location: str = None
    location_link: str = None
    link: str = None
    image_url: str = None
    image_data: str = None
    description:str = ''
    notes: List[str] = []
    changelog: List[ChangeLogEntry] = []

    @property
    def put(self):
        details = {
            'drop_source_format': self.drop_source_format,
            'content': self.content,
            'mob': self.mob,
            'location': self.location,
            'link': self.link,
            'image_url': self.image_url,
            'image_data': self.image_data,
            'description': self.description,
            'notes': self.notes,
            'changelog': [c.put for c in self.changelog],
        }
        return details

    @classmethod
    def build(cls, data):
        details = {}
        if data.get('drop_source_format') is not None:
            details['drop_source_format'] = data['drop_source_format']
        if data.get('content') is not None:
            details['content'] = data['content']
        if data.get('mob') is not None:
            details['mob'] = data['mob']
        if data.get('location') is not None:
            details['location'] = data['location']
        if data.get('location_link') is not None:
            details['location_link'] = data['location_link']
        if data.get('link') is not None:
            details['link'] = data['link']
        if data.get('image_url') is not None:
            details['image_url'] = data['image_url']
        if data.get('image_data') is not None:
            details['image_data'] = data['image_data']
        if data.get('description') is not None:
            details['description'] = data['description']
        if data.get('notes') is not None:
            details['notes'] = data['notes']
        if data.get('changelog') is not None:
            details['changelog'] = [ChangeLogEntry.build(c) for c in data['changelog']]
        return cls(**details)

    def update(self, obj):
        if obj.drop_source_format is not None:
            self.drop_source_format = obj.drop_source_format
        if obj.content is not None:
            self.content = obj.content
        if obj.mob is not None:
            self.mob = obj.mob
        if obj.location is not None:
            self.location = obj.location
        if obj.location_link is not None:
            self.location_link = obj.location_link
        if obj.link is not None:
            self.link = obj.link
        if obj.image_url is not None:
            self.image_url = obj.image_url
        if obj.image_data is not None:
            self.image_data = obj.image_data
        if obj.description is not None:
            self.description = obj.description
        if obj.notes is not None:
            self.notes = obj.notes
        if obj.changelog is not None:
            self.changelog = obj.changelog
        self.changelog.append(ChangeLogEntry(note='Updated'))


class Equipment(BaseModel):
    slot: Slot = Slot.EMPTY
    slot_type: SlotType = SlotType.EMPTY
    elements: List[Element] = [Element.KENETIC]
    name: str = None
    source: EquipmentSource = EquipmentSource()
    manufactures: List[Manufacture] = [Manufacture.UNKNOWN]
    description: str = None
    notes: List[str] = []
    changelog: List[str] = []
    reviewed: bool = False
    locked: bool = False
    # prefix
    # suffex

    @property
    def put(self):
        if self.slot == Slot.EMPTY:
            output = self.slot.name
        else:
            output = {
                'slot': self.slot.name,
                'slot_type': self.slot_type.name,
                'elements': [e.name for e in self.elements],
                'name': self.name,
                'source': self.source.put,
                'manufactures': [m.name for m in self.manufactures],
                'description': self.description,
                'notes': [i for i in self.notes],
                'changelog': [i for i in self.changelog],
                'reviewed': self.reviewed,
                'locked': self.locked,
            }
        return output

    @classmethod
    def build(cls, data):
        details = {
            'slot': getattr(Slot, data['slot']),
        }
        if data.get('slot_type') is not None:
            details['slot_type'] = getattr(SlotType, data['slot_type'])
        if data.get('elements') is not None:
            details['elements'] = [getattr(Element, e) for e in data['elements']]
        if data.get('name') is not None:
            details['name'] = data['name']
        if data.get('source') is not None:
            details['source'] = EquipmentSource.build(data['source'])
        if data.get('manufactures') is not None:
            details['manufactures'] = [getattr(Manufacture, m) for m in data['manufactures']]
        if data.get('description') is not None:
            details['description'] = data['description']
        if data.get('notes') is not None:
            details['notes'] = data['notes']
        if data.get('changelog') is not None:
            details['changelog'] = data['changelog']
        if data.get('reviewed') is not None:
            details['reviewed'] = data['reviewed']
        if data.get('locked') is not None:
            details['locked'] = data['locked']
        return cls(**details)

    def generate_html_tile(self):
        details = Div()
        details.add_class('equipment-tile')
        contents = Paragraph()
        contents.internal.append(f"Type: {self.slot_type.name.replace('_', ' ').title()}")
        contents.internal.append(LineBreak())
        if self.name:
            contents.internal.append(f"Name: {self.name}")
        contents.internal.append(LineBreak())
        elements = []
        for el in self.elements:
            color_item = Link(internal=el.name)
            color_item.add_style(Style(style_details={'color': getattr(ElementColor, el.name).value}))
            # color_item.add_style({'color': getattr(ElementColor, el.name).value})
            elements.append(color_item)
        if elements:
            name = 'Element'
            if len(elements) > 1:
                name += 's'
            contents.internal.append(f'{name}: {" / ".join([e.return_string_version for e in elements])}')
        contents.internal.append(LineBreak())
        if self.source.link:
            link = Link(href=self.source.link, internal='Equipment Link')
            contents.internal.append(link)
        details.internal.append(contents)
        return details


        div = Div()
        div.add_class('equipment-tile')
        content = Paragraph()
        for index, deets in enumerate(data):
            content.internal.append(deets)
            if index >= len(data) - 1:
                content.internal.append(LineBreak())
        div.internal.append(content)
        return ''.join(details)

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def update(self, obj):
        if self.locked:
            return
        if obj.slot is not None:
            self.slot = obj.slot
        if obj.slot_type is not None:
            self.slot_type = obj.slot_type
        if obj.elements is not None:
            self.elements = obj.elements
        if obj.name is not None:
            self.name = obj.name
        if obj.source is not None:
            self.source = obj.source
        if obj.manufactures is not None:
            self.manufactures = obj.manufactures
        if obj.description is not None:
            self.description = obj.description
        if obj.notes is not None:
            self.notes = obj.notes
        if obj.changelog is not None:
            self.changelog = obj.changelog
        if obj.reviewed is not None:
            self.reviewed = obj.reviewed
        self.changelog.append(ChangeLogEntry(note='Updated'))

    def update_from_source(self, obj):
        if self.locked:
            return
        if obj.slot != self.slot:
            self.slot = obj.slot
        if obj.slot_type != self.slot_type:
            self.slot_type = obj.slot_type
        if obj.elements != self.elements:
            self.elements = obj.elements
        if obj.name != self.name:
            self.name = obj.name
        if obj.source != self.source:
            self.source = obj.source
        if obj.manufactures != self.manufactures:
            self.manufactures = obj.manufactures
        if obj.description != self.description:
            self.description = obj.description
        if obj.notes != self.notes:
            for note in obj.notes:
                if note not in self.notes:
                    self.notes.append(note)
        if obj.changelog != self.changelog:
            for cl in obj.changelog:
                if cl not in self.changelog:
                    self.changelog.append(cl)


class BuildLink(BaseModel):
    url: str = None
    description: str = ''
    notes: List[str] = []
    changelog: List[str] = []

    @property
    def put(self):
        output = {
            'url': self.url,
            'description': self.description,
            'notes': self.notes,
            'changelog': self.changelog,
        }
        return output

    @classmethod
    def build(cls, data):
        details = {
            'url': data['url'],
            'description': data['description'],
            'notes': data['notes'],
            'changelog': data['changelog'],
        }
        return cls(**details)


class Character:
    def __init__(
        self,
        vault_hunter: VaultHunter,
        description: str = '',
        gun1: Equipment = Equipment(),
        gun2: Equipment = Equipment(),
        gun3: Equipment = Equipment(),
        gun4: Equipment = Equipment(),
        artifact: Equipment = Equipment(),
        class_mod: Equipment = Equipment(),
        grenade_mod: Equipment = Equipment(),
        shield: Equipment = Equipment(),
        associated_slots: List[Equipment] = [],
        archived_slots: List[Equipment] = [],
        active_build: BuildLink = BuildLink(),
        associated_builds: List[BuildLink] = [],
        archived_builds: List[BuildLink] = [],
        active: bool = True,
        notes: List[str] = [],
        changelog: List[str] = [],
    ):
        self.vault_hunter = vault_hunter
        self.description = description
        self.gun1 = gun1
        self.gun2 = gun2
        self.gun3 = gun3
        self.gun4 = gun4
        self.artifact = artifact
        self.class_mod = class_mod
        self.grenade_mod = grenade_mod
        self.shield = shield
        self.associated_slots = associated_slots
        self.archived_slots = archived_slots
        self.active_build = active_build
        self.associated_builds = associated_builds
        self.archived_builds = archived_builds
        self.active = active
        self.notes = notes
        self.changelog = changelog

    @property
    def put(self):
        details = {
            'vault_hunter': self.vault_hunter.name,
            'description': self.description,
            'gun1': self.gun1.put,
            'gun2': self.gun2.put,
            'gun3': self.gun3.put,
            'gun4': self.gun4.put,
            'artifact': self.artifact.put,
            'class_mod': self.class_mod.put,
            'grenade_mod': self.grenade_mod.put,
            'shield': self.shield.put,
            'associated_slots': [s.put for s in self.associated_slots if s.slot_type != Slot.EMPTY],
            'archived_slots': [s.put for s in self.archived_slots if s.slot_type != Slot.EMPTY],
            'active_build': self.active_build.put,
            'associated_builds': [b.put for b in self.associated_builds],
            'archived_builds': [b.put for b in self.archived_builds],
            'active': self.active,
            'notes': [i for i in self.notes],
            'changelog': [i for i in self.changelog],
        }
        return details

    @classmethod
    def build(cls, data):
        details = {
            'vault_hunter': getattr(VaultHunter, data['vault_hunter'])
        }
        if data.get('description') is not None:
            details['description'] = data['description']
        if data.get('gun1') is not None:
            details['gun1'] = data['gun1']
        if data.get('gun2') is not None:
            details['gun2'] = data['gun2']
        if data.get('gun3') is not None:
            details['gun3'] = data['gun3']
        if data.get('gun4') is not None:
            details['gun4'] = data['gun4']
        if data.get('artifact') is not None:
            details['artifact'] = data['artifact']
        if data.get('class_mod') is not None:
            details['class_mod'] = data['class_mod']
        if data.get('grenade_mod') is not None:
            details['grenade_mod'] = data['grenade_mod']
        if data.get('shield') is not None:
            details['shield'] = data['shield']
        if data.get('associated_slots') is not None:
            details['associated_slots'] = data['associated_slots']
        if data.get('archived_slots') is not None:
            details['archived_slots'] = data['archived_slots']
        if data.get('active_build') is not None:
            details['active_build'] = data['active_build']
        if data.get('associated_builds') is not None:
            details['associated_builds'] = data['associated_builds']
        if data.get('archived_builds') is not None:
            details['archived_builds'] = data['archived_builds']
        if data.get('active') is not None:
            details['active'] = data['active']
        if data.get('notes') is not None:
            details['notes'] = data['notes']
        if data.get('changelog') is not None:
            details['changelog'] = data['changelog']
        return cls(**details)

    def add_equipment(self, equipment: Equipment):
        created = False
        if equipment.slot == Slot.ARTIFACT:
            if self.artifact.slot == Slot.EMPTY:
                self.artifact = equipment
                created = True
        elif equipment.slot == Slot.CLASS_MOD:
            if self.class_mod.slot == Slot.EMPTY:
                self.class_mod = equipment
                created = True
        elif equipment.slot == Slot.GRENADE_MOD:
            if self.grenade_mod.slot == Slot.EMPTY:
                self.grenade_mod = equipment
                created = True
        elif equipment.slot == Slot.SHIELD:
            if self.shield.slot == Slot.EMPTY:
                self.shield = equipment
                created = True
        else:
            for i in range(1,5):
                if getattr(self, f"gun{i}").slot == Slot.EMPTY:
                    setattr(self, f"gun{i}", equipment)
                    created = True
                    break
        if not created:
            self.associated_slots.append(equipment)

    def add_associate(self, equipment: Equipment):
        self.associated_slots.append(equipment)

    def add_archive(self, equipment: Equipment):
        self.archived_slots.append(equipment)

    def generate_html_tile(self):
        details = []
        div = Div()
        div.add_class('tile')
        div.add_style(Style(style_details={'border-color': getattr(VaultHunterColor, self.vault_hunter.name).value}))
        # div.add_style({'border-color': getattr(VaultHunterColor, self.vault_hunter.name).value})
        h1 = Header(1, self.vault_hunter.name.title())
        h1.add_style({'color': getattr(VaultHunterColor, self.vault_hunter.name).value})
        div.internal.append(h1)
        content = Paragraph()
        content.internal.append(self.description)

        if self.active_build:
            content.internal.append(LineBreak())
            link = Link(href=self.active_build.url)
            link.internal.append('Current Build')
            content.internal.append(link)

            if self.active_build.url:
                match = re.search(r'https://www.lootlemon.com/class/[a-z0-9#]+_(\d+)_(\d+)_(\d+)_(\d+)', self.active_build.url)
                if match:
                    groups = match.groups(0)
                    point_item = Div()
                    point_item.add_style({
                        'min-width': '100px',
                        'max-width': '150px',
                    })
                    separator_item = Div(internal='/')
                    separator_item.add_class('build-point-item')
                    separator_item.add_style({
                        'margin': '0px',
                        'padding': '0px',
                    })

                    bracket_item = Div(internal='(')
                    bracket_item.add_style({
                        'margin': '0px',
                        'padding': '0px',
                        'display': 'inline-block'
                    })
                    point_item.internal.append(bracket_item)

                    # First
                    first_tree = Div(internal=f"{sum([int(i) for i in groups[0]])}")
                    first_tree.add_class('build-point-item')
                    first_tree.add_style({'color': 'green'})
                    point_item.internal.append(first_tree)

                    point_item.internal.append(separator_item)

                    # Second
                    second_tree = Div(internal=f"{sum([int(i) for i in groups[1]])}")
                    second_tree.add_class('build-point-item')
                    second_tree.add_style({'color': 'blue'})
                    point_item.internal.append(second_tree)

                    point_item.internal.append(separator_item)

                    # Third
                    third_tree = Div(internal=f"{sum([int(i) for i in groups[2]])}")
                    third_tree.add_class('build-point-item')
                    third_tree.add_style({'color': 'red'})
                    point_item.internal.append(third_tree)

                    point_item.internal.append(separator_item)

                    # Fourth
                    fourth_tree = Div(internal=f"{sum([int(i) for i in groups[3]])}")
                    fourth_tree.add_class('build-point-item')
                    fourth_tree.add_style({'color': 'pink'})
                    point_item.internal.append(fourth_tree)

                    bracket_item = Div(internal=')')
                    bracket_item.add_style({'margin': '0px', 'padding': '0px', 'display': 'inline-block'})
                    point_item.internal.append(bracket_item)

                    content.internal.append(point_item)
                    content.internal.append(LineBreak())

        div.internal.append(content)

        if self.gun1.slot != Slot.EMPTY:
            div.internal.append(LineBreak())
            div.internal.append(self.generate_slot_tile(element=self.gun1, slot='Gun 1'.upper()))

        if self.gun2.slot != Slot.EMPTY:
            div.internal.append(LineBreak())
            div.internal.append(self.generate_slot_tile(element=self.gun2, slot='Gun 2'.upper()))

        if self.gun3.slot != Slot.EMPTY:
            div.internal.append(LineBreak())
            div.internal.append(self.generate_slot_tile(element=self.gun3, slot='Gun 3'.upper()))

        if self.gun4.slot != Slot.EMPTY:
            div.internal.append(LineBreak())
            div.internal.append(self.generate_slot_tile(element=self.gun4, slot='Gun 4'.upper()))

        if self.artifact.slot != Slot.EMPTY:
            div.internal.append(LineBreak())
            div.internal.append(self.generate_slot_tile(element=self.artifact, slot='Artifact'.upper()))

        if self.class_mod.slot != Slot.EMPTY:
            div.internal.append(LineBreak())
            div.internal.append(self.generate_slot_tile(element=self.class_mod, slot='Class Mod'.upper()))

        if self.grenade_mod.slot != Slot.EMPTY:
            div.internal.append(LineBreak())
            div.internal.append(self.generate_slot_tile(element=self.grenade_mod, slot='Grenade Mod'.upper()))

        if self.shield.slot != Slot.EMPTY:
            div.internal.append(LineBreak())
            div.internal.append(self.generate_slot_tile(element=self.shield, slot='Shield'.upper()))

        return div

        if self.associated_builds or self.associated_slots:
            details.append('<h2 class="pageBreak">Associated Items</h2>')
            associated = []
            for index, link in enumerate(self.associated_builds):
                if link.description:
                    desc = link.description
                else:
                    desc = f"Link {index}"
                associated.append(f'<a href="{link.url}">{desc}</a>')

            if self.associated_builds:
                details.append(f'''
                    <div class="dropdown">
                    <button class="dropbtn">Associated Builds</button>
                    <div class="dropdown-content build-link">{''.join(associated)}</div>
                    </div>
                ''')

            if self.associated_builds and self.associated_slots:
                details.append('<br>')

            associated = []
            x=1
            for index, link in enumerate(self.associated_slots):
                x=1
                associated.append(self.generate_slot_tile(element=link))
            if self.associated_slots:
                details.append(f'''
                    <div class="dropdown">
                    <button class="dropbtn">Associated Slots</button>
                    <div class="dropdown-content slot-tile">{''.join(associated)}</div>
                    </div>
                ''')

        if self.archived_builds or self.archived_slots:
            details.append('<h2 class="pageBreak">Archived Items</h2>')
            archived = []
            for index, link in enumerate(self.archived_builds):
                if link.description:
                    desc = link.description
                else:
                    desc = f"Link {index}"
                archived.append(f'<a href="{link.url}">{desc}</a>')
            if self.archived_builds:
                details.append(f'''
                    <div class="dropdown">
                    <button class="dropbtn">Archived Builds</button>
                    <div class="dropdown-content build-link">{''.join(archived)}</div>
                    </div>
                ''')

            if self.archived_builds and self.archived_slots:
                details.append('<br>')

            archived = []
            x=1
            for index, link in enumerate(self.archived_slots):
                x=1
                archived.append(self.generate_slot_tile(element=link))
            if self.archived_slots:
                details.append(f'''
                    <div class="dropdown">
                    <button class="dropbtn">Archived Slots</button>
                    <div class="dropdown-content slot-tile">{''.join(archived)}</div>
                    </div>
                ''')

        details.append('</div>')
        return ''.join(details)

    def generate_slot_tile(self, element, slot=None):
        # tile = []
        # tile.append('<br>')
        # tile.append(f'<h2>{element.slot.value.replace("_", " ").title()}</h2>')
        # tile.append(f'<h2 class="pageBreak">{element.slot.value.replace("_", " ").title()}</h2>')
        tile = Div()
        tile.add_class('slot-tile')
        # tile.append(f'<div class="slot-tile">')
        if slot:
            # tile.append(f'<h2>{slot}</h2>')
            h2 = Header(2, slot)
            tile.internal.append(h2)
        # tile.append(f'{element.generate_html_tile()}')
        tile.internal.append(element.generate_html_tile())
        # tile.append('</div>')
        return tile

class BorderlandsAccountManager:
    def __init__(self, characters: List[Character] = []):
        self.characters = characters

    @property
    def put(self):
        return [c.put for c in self.characters]

    @classmethod
    def build(cls, data=None):
        details = []
        for character in data:
            character['vault_hunter'] = getattr(VaultHunter, character['vault_hunter'])
            character['gun1'] =  Equipment.build(character['gun1'])
            character['gun2'] =  Equipment.build(character['gun2'])
            character['gun3'] =  Equipment.build(character['gun3'])
            character['gun4'] =  Equipment.build(character['gun4'])
            character['artifact'] =  Equipment.build(character['artifact'])
            character['class_mod'] =  Equipment.build(character['class_mod'])
            character['grenade_mod'] =  Equipment.build(character['grenade_mod'])
            character['shield'] =  Equipment.build(character['shield'])
            character['associated_slots'] = [Equipment.build(s) for s in character['associated_slots']]
            character['archived_slots'] = [Equipment.build(s) for s in character['archived_slots']]
            details.append(Character(**character))
        obj = cls(characters=details)
        return obj

    def add_character(self, vault_hunter: VaultHunter | str, descriptor: str):
        if not isinstance(vault_hunter, VaultHunter):
            vault_hunter = getattr(VaultHunter, vault_hunter.upper())
        char = Character(
                vault_hunter=vault_hunter,
                description=descriptor,
            )
        self.characters.append(
            char
        )
        return char

    def find_characters(
        self,
        vault_hunter: VaultHunter | str = None,
        descriptor: str = None,
    ):
        if not isinstance(vault_hunter, VaultHunter):
            vault_hunter = getattr(VaultHunter, vault_hunter.upper())

        skip_chars = []

        for index, char in enumerate(self.characters):
            if vault_hunter:
                if char.vault_hunter != vault_hunter:
                    skip_chars.append(index)
            if descriptor:
                match = re.search(descriptor, char.build_description)
                if not match:
                    skip_chars.append(index)

        skip_chars = set(skip_chars)
        output = []
        for index, char in enumerate(self.characters):
            if index not in skip_chars:
                output.append(char)
        return output

    def save_details(self, filepath: str):
        with open(filepath, 'w') as df:
            df.write(json.dumps(self.put, indent=4))

    def load_details(self, filepath: str):
        with open(filepath, 'r') as df:
            data = json.load(df)
        return BorderlandsAccountManager.build(data)

class EquipmentReview:
    def __init__(self):
        self.equipemnt = []

    def get_equipment_files(self, dir_path=None):
        data = []
        if dir_path is None:
            dir_path = 'html_data'
        for fl in os.listdir(dir_path):
            if not fl.endswith('.json'):
                continue
            with open('html_data/' + fl, 'r') as df:
                equipment_list = json.load(df)
            for equipment_json in equipment_list:
                equipment_obj = Equipment.build(equipment_json)
                data.append(equipment_obj)
        return data

    def save_details(self, filepath: str ='saveoffs/equipment_save.json'):
        data = [e.put for e in self.equipemnt]
        with open(filepath, 'w') as df:
            df.write(json.dumps(data, indent=4))

    def load_details(self, filepath: str ='saveoffs/equipment_save.json'):
        with open(filepath, 'r') as df:
            data = json.load(df)
        return [Equipment.build(e) for e in data]

    def load_data(self):
        equipment_data_file_list = self.load_details()
        equipment_html_files_list = self.get_equipment_files()
        for eq_df in equipment_data_file_list:
            for eq_hf in equipment_html_files_list:
                if (eq_df.name == eq_hf.name) and (eq_df.slot == eq_hf.slot):
                    eq_df.update_from_source(eq_hf)
            self.equipemnt.append(eq_df)
        for eq_hf in equipment_html_files_list:
            dupe = False
            for eq_df in equipment_data_file_list:
                if (eq_df.name == eq_hf.name) and (eq_df.slot == eq_hf.slot):
                    dupe = True
                    continue
            if not dupe:
                self.equipemnt.append(eq_hf)

    def find_equipment(
        self,
        slot: List[Slot] = [None],
        slot_type: List[SlotType] = [None],
        elements: List[Element] = [None],
        name: str = None,
        equipment_source: List[EquipmentSource] = [None],
        manufactures: List[Manufacture] = [None],
        description: str = None,
        reviewed: bool = None,
    ):
        if not isinstance(slot, list):
            slot = [slot]
        if not isinstance(slot_type, list):
            slot_type = [slot_type]
        if not isinstance(elements, list):
            elements = [elements]
        if not isinstance(equipment_source, list):
            equipment_source = [equipment_source]
        if not isinstance(manufactures, list):
            manufactures = [manufactures]

        results = []

        for equipment in self.equipemnt:
            if slot != [None]:
                if not self._valid_equipment(
                    equipment=equipment,
                    equipment_stat='slot',
                    stat_values=slot
                ):
                    continue
            if slot_type != [None]:
                if not self._valid_equipment(
                    equipment=equipment,
                    equipment_stat='slot_type',
                    stat_values=slot_type
                ):
                    continue
            if elements != [None]:
                if not self._valid_equipment(
                    equipment=equipment,
                    equipment_stat='elements',
                    stat_values=elements
                ):
                    continue
            if name is not None:
                match = re.search(name, equipment.name)
                if not match:
                    continue
            if equipment_source != [None]:
                if not self._valid_source_equipment(
                    equipment=equipment,
                    equipment_stat='source',
                    stat_values=equipment_source
                ):
                    continue
            if manufactures != [None]:
                if not self._valid_equipment(
                    equipment=equipment,
                    equipment_stat='manufactures',
                    stat_values=manufactures
                ):
                    continue
            if description is not None:
                match = re.search(description, equipment.description)
                if not match:
                    continue
            if reviewed is not None:
                if reviewed and not equipment.reviewed:
                    continue
                if not reviewed and equipment.reviewed:
                    continue

            results.append(equipment)
        return results

    def _valid_equipment(self, equipment, equipment_stat, stat_values):
        if not isinstance(getattr(equipment, equipment_stat), list):
            equipment_stat_for_validating = [getattr(equipment, equipment_stat)]
        else:
            equipment_stat_for_validating = getattr(equipment, equipment_stat)
        for esfv in equipment_stat_for_validating:
            if esfv in stat_values:
                return True
        return False

    def _valid_source_equipment(self, equipment, equipment_stat, stat_values):
        """
        This will error if it only matches one. So i need to re-think this loop. ugh.
        """
        for stat in stat_values:
            for key, value in EquipmentSource():
                if key in ['notes', 'changelog']:
                    continue
                if getattr(stat, key) is not None:
                    match = re.search(getattr(stat, key), getattr(equipment.source, key))
                    if not match:
                        return False
        return True

    def open_equipment_urls(self, count=5, **kwargs):
        equipment_list = self.find_equipment(**kwargs)
        opened = []
        for equipment in equipment_list[:count]:
            if count < 0:
                break
            url = equipment.source.link
            print(f"Opening equipment: {url}")
            if url is None:
                print(equipment.name)
                continue
            webbrowser.open_new_tab(url)
            opened.append(equipment)
            count -= 1
        return opened
