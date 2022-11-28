from re import S
from pydantic import BaseModel
from typing import List
from enum import Enum


class Element(Enum):
    FIRE = 'fire'
    SHOCK = 'shock'
    ACID = 'acid'
    CRYO = 'cryo'
    RADIATION = 'radiation'
    KENETIC = 'kenetic'


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


class Equipment:
    def __init__(
        self,
        slot: Slot,
        elements: List[Element],
        name: str = '',
        link: str = '',
        description: str = '',
        notes: List[str] = [],
        changelog: List[str] = [],
    ):
        self.slot = slot
        self.name = name
        self.link = link
        self.description = description
        self.elements = elements
        self.notes = notes
        self.changelog = changelog



class Build:

    def __init__(
        self,
        vault_hunter: str = '',
        build_description: str = '',
        active_build: List[str] = [],
        associated_builds: List[str] = [],
        archived_builds: List[str] = [],
        active_slots: List[Equipment] = [],
        associated_slots: List[Equipment] = [],
        archived_slots: List[Equipment] = [],
    ):
        self.vault_hunter = vault_hunter
        self.build_description = build_description
        self.active_build = active_build
        self.associated_builds = associated_builds
        self.archived_builds = archived_builds

        self.active_slots = active_slots
        self.associated_slots = associated_slots
        self.archived_slots = archived_slots

        self.notes = []

        self.changelog = []

    @property
    def artifacts(self):
        return [s for s in self.active_slots if s == Slot.ARTIFACT]

    @property
    def guns(self):
        return [s for s in self.active_slots if s == Slot.GUNS]

    @property
    def class_mods(self):
        return [s for s in self.active_slots if s == Slot.CLASS_MOD]

    @property
    def grenade_mods(self):
        return [s for s in self.active_slots if s == Slot.GRENADE_MOD]

    @property
    def shields(self):
        return [s for s in self.active_slots if s == Slot.SHIELD]

    @property
    def guns(self):
        return [s for s in self.active_slots if s in [
            'assault_rifle',
            'pistol',
            'rocket_launcher',
            'shotgun',
            'smg',
            'sniper_rifle',
        ]]

    @property
    def shields(self):
        return [s for s in self.active_slots if s == 'shield']

    def put(self):
        details = {
            'vault_hunter': self.vault_hunter,
            'build_description': self.build_description,
            'active_build': self.active_build,
            'active_guns': self.active_guns,
            'active_shield': self.active_shield,
            'active_grenade': self.active_grenade,
            'active_relic': self.active_relic,
            'active_artifact': self.active_artifact,
            'active_class_mod': self.active_class_mod,
            'damage_types':{
                'fire_guns': self.fire_guns,
                'shock_guns': self.shock_guns,
                'acid_guns': self.acid_guns,
                'cryo_guns': self.cryo_guns,
                'radiation_guns': self.radiation_guns,
            },
            'gun_types':{
                'assault_rifles': self.assault_rifles,
                'pistols': self.pistols,
                'rocket_launchers': self.rocket_launchers,
                'shotguns': self.shotguns,
                'smgs': self.smgs,
                'sniper_rifles': self.sniper_rifles,
            },
            'notes': self.notes,
        }
        return details

    def full_put(self):
        details = {
            'vault_hunter': self.vault_hunter,
            'build_description': self.build_description,
            'active_build': self.active_build,
            'archived_builds': self.archived_builds,
            'associated_builds': self.associated_builds,
            'active_guns': self.active_guns,
            'associated_guns': self.associated_guns,
            'active_shield': self.active_shield,
            'associated_shields': self.associated_shields,
            'active_grenade': self.active_grenade,
            'associated_grenades': self.associated_grenades,
            'active_relic': self.active_relic,
            'associated_relics': self.associated_relics,
            'active_artifact': self.active_artifact,
            'associated_artifacts': self.associated_artifacts,
            'active_class_mod': self.active_class_mod,
            'associated_class_mods': self.associated_class_mods,
            'fire_guns': self.fire_guns,
            'shock_guns': self.shock_guns,
            'acid_guns': self.acid_guns,
            'cryo_guns': self.cryo_guns,
            'radiation_guns': self.radiation_guns,
            'assault_rifles': self.assault_rifles,
            'pistols': self.pistols,
            'rocket_launchers': self.rocket_launchers,
            'shotguns': self.shotguns,
            'smgs': self.smgs,
            'sniper_rifles': self.sniper_rifles,
            'notes': self.notes,
            'changelog': self.changelog,
        }
        return details

    def create_equipment(self, slot, name=None, link=None, elements=[]):
        if not isinstance(slot, Slot):
            if slot in ['artifact']:
                slot = 'artifact'
            if slot in ['assault_rifle', 'assault']:
                slot = 'assault_rifle'
            if slot in ['class_mod', 'class']:
                slot = 'class_mod'
            if slot in ['grenade_mod', 'grenade']:
                slot = 'grenade_mod'
            if slot in ['pistol']:
                slot = 'pistol'
            if slot in ['rocket_launcher', 'launcher']:
                slot = 'rocket_launcher'
            if slot in ['shield']:
                slot = 'shield'
            if slot in ['shotgun']:
                slot = 'shotgun'
            if slot in ['smg']:
                slot = 'smg'
            if slot in ['sniper_rifle', 'sniper']:
                slot = 'sniper_rifle'
            slot = getattr(Slot, slot.upper())
        details = {
            'slot': slot,
            'elements': [],
        }
        if name:
            details['name'] = name
        elif link:
            details['link'] = link
        else:
            return
        for element in elements:
            if isinstance(element, Element):
                details['elements'].append(element)
            else:
                details['elements'].append(getattr(Element, element.upper()))
        return Equipment(**details)

    def add_active(self, slot: Slot | str, name: str = None, link: str = None, elements: List[Element | str] = []):
        self.active_slots.append(
            self.create_equipment(slot, name, link, elements)
        )
