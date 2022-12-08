from operator import eq
from tkinter import E
from unittest import skip
from pydantic import BaseModel
from typing import List
from enum import Enum
import json
import re


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
    ARTIFACT = 'artifact'
    ASSAULT_RIFLE = 'assault_rifle'
    CLASS_MOD = 'class_mod'
    GRENADE_MOD = 'grenade_mod'
    PISTOL = 'pistol'
    ROCKET_LAUNCHER = 'rocket_launcher'
    SHIELD = 'shield'
    SHOTGUN = 'shotgun'
    SMG = 'smg'
    SNIPER_RIFLE = 'sniper_rifle'
    EMPTY = None


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


class Equipment(BaseModel):
    slot: Slot = Slot.EMPTY
    elements: List[Element] = [Element.KENETIC]
    name: str = ''
    link: str = ''
    description: str = ''
    notes: List[str] = []
    changelog: List[str] = []
    # prefix
    # suffex

    @property
    def put(self):
        if self.slot == Slot.EMPTY:
            output = self.slot.name
        else:
            output = {
                'slot': self.slot.name,
                'elements': [e.name for e in self.elements],
                'name': self.name,
                'link': self.link,
                'description': self.description,
                'notes': [i for i in self.notes],
                'changelog': [i for i in self.changelog],
            }
        return output

    @classmethod
    def build(cls, data):
        details = {
            'slot': getattr(Slot, data['slot']),
            'elements': [getattr(Element, e) for e in data['elements']],
            'name': data['name'],
            'link': data['link'],
            'description': data['description'],
            'notes': data['notes'],
            'changelog': data['changelog'],
        }
        return cls(**details)

    def generate_html_tile(self):
        details = []
        details.append('<div class="equipment-tile">')
        details.append('<p>')
        data = []
        data.append(f"Type: {self.slot.name.replace('_', ' ').title()}")
        if self.name:
        #     details.append('</br>')
            data.append(f"Name: {self.name}")
        elements = []
        for el in self.elements:
            elements.append(f'<a style="color:{getattr(ElementColor, el.name).value};">{el.name}</a>')
        if elements:
        #     details.append('</br>')
            name = 'Element'
            if len(elements) > 1:
                name += 's'
            data.append(f'{name}: {" / ".join(elements)}')
        if self.link:
        #     details.append('</br>')
            data.append(f'Link: <a href="{self.link}">Equipment Link</a>')
        details.append('<br>'.join(data))
        details.append('</p>')
        details.append('</div>')
        return ''.join(details)


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
            'associated_slots': [s.put for s in self.associated_slots if s.slot != Slot.EMPTY],
            'archived_slots': [s.put for s in self.archived_slots if s.slot != Slot.EMPTY],
            'active_build': self.active_build.put,
            'associated_builds': [b.put for b in self.associated_builds],
            'archived_builds': [b.put for b in self.archived_builds],
            'active': self.active,
            'notes': [i for i in self.notes],
            'changelog': [i for i in self.changelog],
        }
        return details

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
        # details.append(f'<div class=tile fill-style: solid; fill-color: {getattr(VaultHunterColor, self.vault_hunter.name).value};>')
        # details.append(f'<div class=tile; border-color: {getattr(VaultHunterColor, self.vault_hunter.name).value};>')
        details.append(f'<div class=tile style="border-color: {getattr(VaultHunterColor, self.vault_hunter.name).value};">')
        # a = getattr(VaultHunterColor, self.vault_hunter.name).value
        details.append(f'<h1 style="color:{getattr(VaultHunterColor, self.vault_hunter.name).value};">{self.vault_hunter.name.title()}</h1>')
        # details.append(f"<h1>{self.vault_hunter.name.title()}</h1>")
        # details.append('<br>')
        # details.append('<br>')
        details.append(f"<p>")
        details.append(f"{self.description}")
        
        if self.active_build:
            details.append('<br>')
            # details.append(f'</p>')
            details.append(f'<a href="{self.active_build.url}">Current Build</a>    ')
            # details.append('<br>')

            if self.active_build.url:
                match = re.search(r'https://www.lootlemon.com/class/[a-z0-9#]+_(\d+)_(\d+)_(\d+)_(\d+)', self.active_build.url)
                if match:
                    # details.append(f'<br>')
                    groups = match.groups(0)
                    details.append(f'<a>( </a>')
                    details.append(f'<a style="color:green;">{sum([int(i) for i in groups[0]])}</a>')
                    details.append(f'<a> / </a>')
                    details.append(f'<a style="color:blue;">{sum([int(i) for i in groups[1]])}</a>')
                    details.append(f'<a> / </a>')
                    details.append(f'<a style="color:red;">{sum([int(i) for i in groups[2]])}</a>')
                    details.append(f'<a> / </a>')
                    details.append(f'<a style="color:pink;">{sum([int(i) for i in groups[3]])}</a>')
                    details.append(f'<a> )</a>')
                    details.append(f'<br>')
                # details.append(f'</p>')
        details.append(f"</p>")

        if self.gun1.slot != Slot.EMPTY:
            details.append('<br>')
            details.append(self.generate_slot_tile(element=self.gun1, slot='Gun 1'.upper()))

        if self.gun2.slot != Slot.EMPTY:
            details.append('<br>')
            details.append(self.generate_slot_tile(element=self.gun2, slot='Gun 2'.upper()))

        if self.gun3.slot != Slot.EMPTY:
            details.append('<br>')
            details.append(self.generate_slot_tile(element=self.gun3, slot='Gun 3'.upper()))

        if self.gun4.slot != Slot.EMPTY:
            details.append('<br>')
            details.append(self.generate_slot_tile(element=self.gun4, slot='Gun 4'.upper()))

        if self.artifact.slot != Slot.EMPTY:
            details.append('<br>')
            details.append(self.generate_slot_tile(element=self.artifact, slot='Artifact'.upper()))

        if self.class_mod.slot != Slot.EMPTY:
            details.append('<br>')
            details.append(self.generate_slot_tile(element=self.class_mod, slot='Class Mod'.upper()))

        if self.grenade_mod.slot != Slot.EMPTY:
            details.append('<br>')
            details.append(self.generate_slot_tile(element=self.grenade_mod, slot='Grenade Mod'.upper()))

        if self.shield.slot != Slot.EMPTY:
            details.append('<br>')
            details.append(self.generate_slot_tile(element=self.shield, slot='Shield'.upper()))

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
        tile = []
        # tile.append('<br>')
        # tile.append(f'<h2>{element.slot.value.replace("_", " ").title()}</h2>')
        # tile.append(f'<h2 class="pageBreak">{element.slot.value.replace("_", " ").title()}</h2>')
        tile.append(f'<div class="slot-tile">')
        if slot:
            tile.append(f'<h2>{slot}</h2>')
        tile.append(f'{element.generate_html_tile()}')
        tile.append('</div>')
        # tile.append(element.generate_html_tile())
        return ''.join(tile)

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
