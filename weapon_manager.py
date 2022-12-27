from datetime import datetime

import json

from classes import (
    ChangeLogEntry,
    Element,
    ElementColor,
    Slot,
    SlotType,
    VaultHunter,
    VaultHunterColor,
    Equipment,
    EquipmentSource,
    BuildLink,
    Character,
    BorderlandsAccountManager,
    EquipmentReview,
)
from html_generator import(
    CharacterHTML
)

er = EquipmentReview()
data = er.load_equipment_file()
# data2 = er.find_equipment(
#     slot=Slot.SHIELD
# )
data3 = er.find_equipment(
    slot_type=SlotType.ASSAULT_RIFLE,
)
d3 = [d.name for d in data3]

no_pew_pew = Equipment(
    slot=Slot.WEAPON,
    slot_type=SlotType.ASSAULT_RIFLE,
    elements=[Element.FIRE],
    name='NoPewPew',
    source=EquipmentSource(
        drop_source_format='World Drop',
        content='Cartels Event',
        mob='Joey Ultraviolet',
        link='https://borderlands.fandom.com/wiki/NoPewPew',
        description='Extra, Extra spicy.',
    )
)
x=1
er.equipemnt.append(no_pew_pew)

data4 = er.find_equipment(
    slot_type=SlotType.ASSAULT_RIFLE,
)
d4 = [d.name for d in data4]
x=1

data4 = er.find_equipment(
    slot_type=SlotType.ASSAULT_RIFLE,
)

x=1

