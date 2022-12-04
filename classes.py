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
    AMARA = 'purple'
    FL4K = 'green'
    MOZE = 'red'
    ZANE = 'blue'


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
        details.append('<div>')
        details.append(f"{self.slot.name.replace('_', ' ').title()}")
        details.append('</br>')
        details.append(f"{self.name}")
        details.append('</br>')
        elements = []
        for el in self.elements:
            elements.append(f'<a style="color:{getattr(ElementColor, el.name).value};">{el.name}</a>')
        details.append('/'.join(elements))
        details.append('</div>')
        return ''.join(details)


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
        active_build: str = None,
        associated_builds: List[str] = [],
        archived_builds: List[str] = [],
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
            'active_build': self.active_build,
            'associated_builds': [b for b in self.associated_builds],
            'archived_builds': [b for b in self.archived_builds],
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
        details.append('<div class=tile>')
        details.append(f"{self.vault_hunter.name.title()}")
        details.append('</br>')
        details.append(f"{self.description}")
        if self.active_build:
            details.append('</br>')
            details.append(f'</p>')
            details.append(f'<a href="{self.active_build}">Current Build</a>')
            'https://www.lootlemon.com/class/fl4k#bgef_505525130051_5055351351311_000000000000_00000000000000'
            match = re.search(r'https://www.lootlemon.com/class/[a-z0-9#]+_(\d+)_(\d+)_(\d+)_(\d+)', self.active_build)
            if match:
                groups = match.groups(0)
                details.append(f'</br>')
                details.append(f'<a>(</a>')
                details.append(f'<a style="color:green;">{sum([int(i) for i in groups[0]])}</a>')
                details.append(f'<a>-</a>')
                details.append(f'<a style="color:blue;">{sum([int(i) for i in groups[1]])}</a>')
                details.append(f'<a>-</a>')
                details.append(f'<a style="color:red;">{sum([int(i) for i in groups[2]])}</a>')
                details.append(f'<a>-</a>')
                details.append(f'<a style="color:pink;">{sum([int(i) for i in groups[3]])}</a>')
                details.append(f'<a>)</a>')
                details.append(f'</br>')
            details.append(f'</p>')
        if self.gun1.slot != Slot.EMPTY:
            details.append('</br>')
            details.append('Gun 1')
            details.append(self.gun1.generate_html_tile())
        if self.gun2.slot != Slot.EMPTY:
            details.append('</br>')
            details.append('Gun 2')
            details.append(self.gun2.generate_html_tile())
        if self.gun3.slot != Slot.EMPTY:
            details.append('</br>')
            details.append('Gun 3')
            details.append(self.gun3.generate_html_tile())
        if self.gun4.slot != Slot.EMPTY:
            details.append('</br>')
            details.append('Gun 4')
            details.append(self.gun4.generate_html_tile())
        if self.artifact.slot != Slot.EMPTY:
            details.append('</br>')
            details.append('Artifact')
            details.append(self.artifact.generate_html_tile())
        if self.class_mod.slot != Slot.EMPTY:
            details.append('</br>')
            details.append('Class Mod')
            details.append(self.class_mod.generate_html_tile())
        if self.grenade_mod.slot != Slot.EMPTY:
            details.append('</br>')
            details.append('Grenade Mod')
            details.append(self.grenade_mod.generate_html_tile())
        if self.shield.slot != Slot.EMPTY:
            details.append('</br>')
            details.append('Shield')
            details.append(self.shield.generate_html_tile())

        details.append('</div>')
        return ''.join(details)


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
