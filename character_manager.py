from datetime import datetime

import json

from classes import (
    ChangeLogEntry,
    Element,
    ElementColor,
    Manufacture,
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
data2 = er.find_equipment(
    slot=Slot.SHIELD
)
data3 = er.find_equipment(
    # slot_type=SlotType.ASSAULT_RIFLE,
    manufactures=[Manufacture.COV]
)
d3 = [d.name for d in data3]

x=1

bam = BorderlandsAccountManager()

# FL4K Main build
char = bam.add_character(vault_hunter='FL4K', descriptor='Pet Build')
char.active_build = BuildLink(
    url='https://www.lootlemon.com/class/fl4k#https://www.lootlemon.com/class/fl4k#bxxf_005505100000_5050351351301_500000000000_54200301002000',
    description='Pet focused DPS'
)



# char.associated_builds = [
#     BuildLink(url='https://www.lootlemon.com/class/fl4k#bgef_505525130051_5055351351311_000000000000_00000000000000', description='Non DLC Pet DPS'),
# ]
# char.archived_builds = [
#     BuildLink(url='https://www.lootlemon.com/class/fl4k#bxxf_005505100000_5050351351301_500000000000_54200301002000', description='Unused build'),
#     BuildLink(url='https://www.lootlemon.com/class/fl4k#beff_005505100000_5050351351301_500000000000_54400301000000', description='Unused build'),
#     BuildLink(url='https://www.lootlemon.com/class/fl4k#beff_035505103501_5050351301000_500000000000_50500301000000', description='Unused build'),
# ]
# char.add_equipment(
#     Equipment(
#         slot=Slot.WEAPON,
#         slot_type=SlotType.ASSAULT_RIFLE,
#         elements=[Element.FIRE],
#         name='NoPewPew',
#         description='Fast firing fire gun',
#         source=EquipmentSource(link='https://www.lootlemon.com/weapon/nopewpew-bl3'),
#     )
# )
# char.add_equipment(
#     Equipment(
#         slot=Slot.WEAPON,
#         slot_type=SlotType.SMG,
#         elements=[Element.SHOCK,
#         Element.FIRE],
#         name='Expert Hellshock',
#         description='A solid shield dropping gun'
#     )
# )
# char.add_equipment(
#     Equipment(
#         slot=Slot.WEAPON,
#         slot_type=SlotType.ASSAULT_RIFLE,
#         elements=[Element.ACID],
#         name='Breath of the Dying',
#         description='Solid Acid gun'
#     )
# )
# char.add_equipment(
#     Equipment(
#         slot=Slot.WEAPON,
#         slot_type=SlotType.SNIPER_RIFLE,
#         elements=[Element.SHOCK],
#         name='Expert Storm',
#         description='Primary sniper'
#     )
# )
# char.add_equipment(
#     Equipment(
#         slot=Slot.SHIELD,
#         slot_type=SlotType.SHIELD,
#         elements=[Element.SHOCK],
#         name='Absorbing Messy Breakup',
#         description='A shield that shoots at enemies and absorbs bullets'
#     )
# )
# char.add_equipment(
#     Equipment(
#         slot=Slot.CLASS_MOD,
#         slot_type=SlotType.CLASS_MOD,
#         name='Showboating Red Fang',
#         description='Gamma Burst, pet taunts and +7 grenade capacity'
#     )
# )
# char.add_equipment(
#     Equipment(
#         slot=Slot.GRENADE_MOD,
#         slot_type=SlotType.GRENADE_MOD,
#         elements=[Element.FIRE],
#         name='Firestorm',
#         description='A lot of damage but also doesnt kill me'
#     )
# )
# char.add_equipment(
#     Equipment(
#         slot=Slot.ARTIFACT,
#         slot_type=SlotType.ARTIFACT,
#         name='Rear Ender Safeguard',
#         description='Creates a shield on ground slam'
#     )
# )

# char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.SNIPER_RIFLE, elements=[Element.CRYO], name='Arctic Tamed Stalker', description='Alternative sniper'))
# char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.SNIPER_RIFLE, elements=[Element.FIRE], name='Stark Krakatoa', description='Alternative sniper'))
# char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.PISTOL, elements=[Element.ACID], name='Venomous Hornet', description='An alternative to the Breat of the Dying'))
# char.archived_slots.append(Equipment(slot=Slot.WEAPON, slot_type=SlotType.ASSAULT_RIFLE, elements=[Element.FIRE], name='NoPewPew', description='Fast firing fire gun'))

# # # For testing only
# # char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.SMG, elements=[Element.CRYO, Element.RADIATION], name='Binary Superflous Devoted', description='Nothing Special')
# # # print(json.dumps(char.put, indent=4))
# # # x=1


# char = bam.add_character(vault_hunter='MOZE', descriptor='MAIN Nuke Build')
# char.active_build = BuildLink(url='https://www.lootlemon.com/class/moze#xxxx_0000000000000_5350553050151_0150000000000_3353001541001')
# char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.ASSAULT_RIFLE, elements=[Element.FIRE], name='NoPewPew', description='Fast firing fire gun'))
# char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.ASSAULT_RIFLE, elements=[Element.RADIATION], name='Double-Penetrating Gross Bearcat', description='Grenade gun for shields'))
# char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.ASSAULT_RIFLE, elements=[Element.CRYO], name='Double-Penetrating Gross Bearcat', description='Grenade gun for armor'))
# char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.ROCKET_LAUNCHER, elements=[Element.KENETIC], name='Tunguska', description='Large AOE damager'))
# char.add_equipment(Equipment(slot=Slot.SHIELD, slot_type=SlotType.SHIELD, elements=[Element.FIRE], name='Bloated Front Loader', description='Reduces action skill cooldown'))
# char.add_equipment(Equipment(slot=Slot.CLASS_MOD, slot_type=SlotType.CLASS_MOD, name='Growling Reinforced Bear Trooper', description='Build centered class mod'))
# char.add_equipment(Equipment(slot=Slot.GRENADE_MOD, slot_type=SlotType.GRENADE_MOD, name='Tran-fusion Tracker', description='Healing grenade'))
# char.add_equipment(Equipment(slot=Slot.ARTIFACT, slot_type=SlotType.ARTIFACT, name='Ravaging Last Stand', description='Nothing special. Eventually find a new one'))


# char = bam.add_character(vault_hunter='ZANE', descriptor='MAIN Speedy Boy')
# char.active_build = BuildLink(url='https://www.lootlemon.com/class/zane#xxxxxx_00000000000000_50551015501_50030500000000_500135155301')
# char.archived_builds = [
#     BuildLink(url='https://www.lootlemon.com/class/zane#xxxxxx_50553011513131_55551015531_00000000000000_000000000000'),
#     BuildLink(url='https://www.lootlemon.com/class/zane#aabdtr_50000000000000_55551515501_00000000000000_500135105331'),
# ]
# char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.SHOTGUN, elements=[Element.FIRE], name='Speedloadn Hellwalker', description='Shotgun with high damange'))
# char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.PISTOL, elements=[Element.RADIATION], name='Nuclear Infinity', description='A shield gun that never reloads'))
# char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.SMG, elements=[Element.CRYO, Element.RADIATION], name='Binary Superflous Devoted', description='Nothing Special'))
# char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.SHOTGUN, elements=[Element.SHOCK], name='The Lab', description='Shotgun with high damange'))
# char.add_equipment(Equipment(slot=Slot.SHIELD, slot_type=SlotType.SHIELD, elements=[Element.FIRE], name='Snap-Shot Whiskey Tango Foxtrot', description='Shotgun with high damange'))
# char.add_equipment(Equipment(slot=Slot.CLASS_MOD, slot_type=SlotType.CLASS_MOD, name='Shockwave Smashing Antifreeze', description='increased damage while sliding or in the air'))
# char.add_equipment(Equipment(slot=Slot.GRENADE_MOD, slot_type=SlotType.GRENADE_MOD, name='Tinas Hippity Hopper', description='Just an unused grenade'))
# char.add_equipment(Equipment(slot=Slot.ARTIFACT, slot_type=SlotType.ARTIFACT, name='Hasty Snowdrift', description='A more useful snowdrift but this is awesome'))


# char = bam.add_character(vault_hunter='AMARA', descriptor='MAIN Melee Build')
# char.active_build = BuildLink(url='https://www.lootlemon.com/class/amara#efd_53000531300501_5050051033031_5000100000000_0500331000000')
# char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.SHOTGUN, elements=[Element.FIRE], name='Speedloadn Hellwalker', description='Shotgun with high damange'))
# char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.SMG, elements=[Element.SHOCK, Element.FIRE], name='Expert Hellshock', description='A solid shield dropping gun'))
# char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.PISTOL, elements=[Element.ACID], name='Venomous Hornet', description='An alternative to the Breat of the Dying'))
# char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.ASSAULT_RIFLE, elements=[Element.KENETIC], name='Blade Fury', description='Shoots melee damage'))
# # char.add_equipment(Equipment(slot=Slot.SHIELD, slot_type=SlotType.SHIELD, elements=[Element.SHOCK], name='Absorbing Messy Breakup', description='A shield that shoots at enemies and absorbs bullets'))
# # char.add_equipment(Equipment(slot=Slot.CLASS_MOD, slot_type=SlotType.CLASS_MOD, name='Showboating Red Fang', description='Gamma Burst, pet taunts and +7 grenade capacity'))
# # char.add_equipment(Equipment(slot=Slot.GRENADE_MOD, slot_type=SlotType.GRENADE_MOD, elements=[Element.FIRE], name='Firestorm', description='A lot of damage but also doesnt kill me'))
# char.add_equipment(Equipment(slot=Slot.ARTIFACT, slot_type=SlotType.ARTIFACT, name='Knife Drain White Elephant', description='Melee damage and heals on melee damage'))

# # https://borderlands.fandom.com/wiki/Fish_Slap
# # https://borderlands.fandom.com/wiki/Unleash_the_Dragon



# # Pointy Psycho Stabber
# # Redundant Face-puncher
# # Brawler Ward
# # Flurrying Solidary Breaker
# # Unlease the Dragon
# # Rain Firestorm


# # 'https://www.lootlemon.com/class/amara#bad_53000531301511_4050051010000_0000000000000_0530331503030'
# # 'https://www.lootlemon.com/class/amara#ead_53000531301511_5040051010000_0000000000000_0503331250031'

# char = bam.add_character(vault_hunter='FL4K', descriptor='Sniper')
# char.active = False





# char = bam.add_character(vault_hunter='MOZE', descriptor='Boss Killer')
# char.active = False





# char = bam.add_character(vault_hunter='MOZE', descriptor='Iron Cub')
# char.active = False





# char = bam.add_character(vault_hunter='AMARA', descriptor='Big Damage')
# char.active = False

bam.save_details(filepath='saveoffs/character_data.json')
x=1
