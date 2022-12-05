from unittest import TestCase
from unittest.mock import MagicMock, call

import json

from classes import (
    Element,
    ElementColor,
    Slot,
    VaultHunter,
    VaultHunterColor,
    Equipment,
    BuildLink,
    Character,
    BorderlandsAccountManager,
)
from html_generator import(
    CharacterHTML
)


def generate_artifact():
    return Equipment(slot=Slot.ARTIFACT)

def generate_assault_rifle():
    return Equipment(slot=Slot.ASSAULT_RIFLE)

def generate_class_mod():
    return Equipment(slot=Slot.CLASS_MOD)

def generate_grenade_mod():
    return Equipment(slot=Slot.GRENADE_MOD)

def generate_pistol():
    return Equipment(slot=Slot.PISTOL)

def generate_rocket_launcher():
    return Equipment(slot=Slot.ROCKET_LAUNCHER)

def generate_shield():
    return Equipment(slot=Slot.SHIELD)

def generate_shotgun():
    return Equipment(slot=Slot.SHOTGUN)

def generate_smg():
    return Equipment(slot=Slot.SMG)

def generate_sniper_rifle():
    return Equipment(slot=Slot.SNIPER_RIFLE)

def generate_None():
    return Equipment(slot=Slot.EMPTY)


# bam = BorderlandsAccountManager()
# x=1
# print(json.dumps(bam.put, indent=4))
# x=1
# bam.add_character(vault_hunter='moze', descriptor='Nuke Build')
# a = bam.find_characters(vault_hunter='moze')[0]
# a.add_equipment(equipment=generate_artifact())
# a.add_equipment(equipment=generate_assault_rifle())
# a.add_equipment(equipment=generate_class_mod())
# a.add_equipment(equipment=generate_grenade_mod())
# a.add_equipment(equipment=generate_pistol())
# a.add_equipment(equipment=generate_rocket_launcher())
# a.add_equipment(equipment=generate_shield())
# a.add_equipment(equipment=generate_shotgun())
# a.add_equipment(equipment=generate_smg())
# a.add_equipment(equipment=generate_sniper_rifle())
# a.add_equipment(equipment=generate_None())

# equip = generate_artifact()
# equip.description = 'Associate only'
# a.add_associate(equipment=equip)
# equip = generate_artifact()
# equip.description = 'Archive only'
# a.add_archive(equipment=equip)
# a.add_archive(equipment=generate_None())

# x=1
# print(json.dumps(bam.put, indent=4))
# x=1
# bam.save_details(filepath='saveoffs/this.json')
# bam2 = bam.load_details(filepath='saveoffs/this.json')
# print(json.dumps(bam2.put, indent=4))
# x=1


bam = BorderlandsAccountManager()

char = bam.add_character(vault_hunter='FL4K', descriptor='MAIN Pet Build')
x=1
char.active_build = BuildLink(url='https://www.lootlemon.com/class/fl4k#https://www.lootlemon.com/class/fl4k#bxxf_005505100000_5050351351301_500000000000_54200301002000', description='Pet focused DPS')
char.associated_builds = [
    BuildLink(url='https://www.lootlemon.com/class/fl4k#bgef_505525130051_5055351351311_000000000000_00000000000000', description='Non DLC Pet DPS'),
]
char.archived_builds = [
    BuildLink(url='https://www.lootlemon.com/class/fl4k#bxxf_005505100000_5050351351301_500000000000_54200301002000', description='Unused build'),
    BuildLink(url='https://www.lootlemon.com/class/fl4k#beff_005505100000_5050351351301_500000000000_54400301000000', description='Unused build'),
    BuildLink(url='https://www.lootlemon.com/class/fl4k#beff_035505103501_5050351301000_500000000000_50500301000000', description='Unused build'),
]
char.add_equipment(Equipment(slot=Slot.ASSAULT_RIFLE, elements=[Element.FIRE], name='NoPewPew', description='Fast firing fire gun', link='https://www.lootlemon.com/weapon/nopewpew-bl3'))
char.add_equipment(Equipment(slot=Slot.SMG, elements=[Element.SHOCK, Element.FIRE], name='Expert Hellshock', description='A solid shield dropping gun', link='https://www.lootlemon.com/weapon/hellshock-bl3'))
char.add_equipment(Equipment(slot=Slot.ASSAULT_RIFLE, elements=[Element.ACID], name='Breath of the Dying', description='Solid Acid gun', link='https://www.lootlemon.com/weapon/breath-of-the-dying-bl3'))
char.add_equipment(Equipment(slot=Slot.SNIPER_RIFLE, elements=[Element.SHOCK], name='Expert Storm', description='Primary sniper', link='https://www.lootlemon.com/weapon/storm-bl3'))
char.add_equipment(Equipment(slot=Slot.SHIELD, elements=[Element.SHOCK], name='Absorbing Messy Breakup', description='A shield that shoots at enemies and absorbs bullets'))
char.add_equipment(Equipment(slot=Slot.CLASS_MOD, name='Showboating Red Fang', description='Gamma Burst, pet taunts and +7 grenade capacity'))
char.add_equipment(Equipment(slot=Slot.GRENADE_MOD, elements=[Element.FIRE], name='Firestorm', description='A lot of damage but also doesnt kill me'))
char.add_equipment(Equipment(slot=Slot.ARTIFACT, name='Rear Ender Safeguard', description='Creates a shield on ground slam'))

char.add_equipment(Equipment(slot=Slot.SNIPER_RIFLE, elements=[Element.CRYO], name='Arctic Tamed Stalker', description='Alternative sniper'))
char.add_equipment(Equipment(slot=Slot.SNIPER_RIFLE, elements=[Element.FIRE], name='Stark Krakatoa', description='Alternative sniper'))
char.add_equipment(Equipment(slot=Slot.PISTOL, elements=[Element.ACID], name='Venomous Hornet', description='An alternative to the Breat of the Dying'))
char.archived_slots.append(Equipment(slot=Slot.ASSAULT_RIFLE, elements=[Element.FIRE], name='NoPewPew', description='Fast firing fire gun', link='https://www.lootlemon.com/weapon/nopewpew-bl3'))
# print(json.dumps(char.put, indent=4))
# x=1


char = bam.add_character(vault_hunter='MOZE', descriptor='MAIN Nuke Build')
char.active_build = BuildLink(url='https://www.lootlemon.com/class/moze#xxxx_0000000000000_5350553050151_0150000000000_3353001541001')
char.add_equipment(Equipment(slot=Slot.ASSAULT_RIFLE, elements=[Element.FIRE], name='NoPewPew', description='Fast firing fire gun'))
char.add_equipment(Equipment(slot=Slot.ASSAULT_RIFLE, elements=[Element.RADIATION], name='Double-Penetrating Gross Bearcat', description='Grenade gun for shields'))
char.add_equipment(Equipment(slot=Slot.ASSAULT_RIFLE, elements=[Element.CRYO], name='Double-Penetrating Gross Bearcat', description='Grenade gun for armor'))
char.add_equipment(Equipment(slot=Slot.ROCKET_LAUNCHER, elements=[Element.KENETIC], name='Tunguska', description='Large AOE damager'))
char.add_equipment(Equipment(slot=Slot.SHIELD, elements=[Element.FIRE], name='Bloated Front Loader', description='Reduces action skill cooldown'))
char.add_equipment(Equipment(slot=Slot.CLASS_MOD, name='Growling Reinforced Bear Trooper', description='Build centered class mod'))
char.add_equipment(Equipment(slot=Slot.GRENADE_MOD, name='Tran-fusion Tracker', description='Healing grenade'))
char.add_equipment(Equipment(slot=Slot.ARTIFACT, name='Ravaging Last Stand', description='Nothing special. Eventually find a new one'))


char = bam.add_character(vault_hunter='ZANE', descriptor='MAIN Speedy Boy')
char.active_build = BuildLink(url='https://www.lootlemon.com/class/zane#xxxxxx_00000000000000_50551015501_50030500000000_500135155301')
char.archived_builds = [
    BuildLink(url='https://www.lootlemon.com/class/zane#xxxxxx_50553011513131_55551015531_00000000000000_000000000000'),
    BuildLink(url='https://www.lootlemon.com/class/zane#aabdtr_50000000000000_55551515501_00000000000000_500135105331'),
]
char.add_equipment(Equipment(slot=Slot.SHOTGUN, elements=[Element.FIRE], name='Speedloadn Hellwalker', description='Shotgun with high damange'))
char.add_equipment(Equipment(slot=Slot.PISTOL, elements=[Element.RADIATION], name='Nuclear Infinity', description='A shield gun that never reloads'))
char.add_equipment(Equipment(slot=Slot.SMG, elements=[Element.CRYO, Element.RADIATION], name='Binary Superflous Devoted', description='Nothing Special'))
char.add_equipment(Equipment(slot=Slot.SHOTGUN, elements=[Element.SHOCK], name='The Lab', description='Shotgun with high damange'))
char.add_equipment(Equipment(slot=Slot.SHIELD, elements=[Element.FIRE], name='Snap-Shot Whiskey Tango Foxtrot', description='Shotgun with high damange'))
char.add_equipment(Equipment(slot=Slot.CLASS_MOD, name='Shockwave Smashing Antifreeze', description='increased damage while sliding or in the air'))
char.add_equipment(Equipment(slot=Slot.GRENADE_MOD, name='Tinas Hippity Hopper', description='Just an unused grenade'))
char.add_equipment(Equipment(slot=Slot.ARTIFACT, name='Hasty Snowdrift', description='A more useful snowdrift but this is awesome'))


char = bam.add_character(vault_hunter='AMARA', descriptor='MAIN Melee Build')
char.active_build = BuildLink(url='https://www.lootlemon.com/class/amara#efd_53000531300501_5050051033031_5000100000000_0500331000000')
char.add_equipment(Equipment(slot=Slot.SHOTGUN, elements=[Element.FIRE], name='Speedloadn Hellwalker', description='Shotgun with high damange'))
char.add_equipment(Equipment(slot=Slot.SMG, elements=[Element.SHOCK, Element.FIRE], name='Expert Hellshock', description='A solid shield dropping gun'))
char.add_equipment(Equipment(slot=Slot.PISTOL, elements=[Element.ACID], name='Venomous Hornet', description='An alternative to the Breat of the Dying'))
char.add_equipment(Equipment(slot=Slot.ASSAULT_RIFLE, elements=[Element.KENETIC], name='Blade Fury', description='Shoots melee damage'))
# char.add_equipment(Equipment(slot=Slot.SHIELD, elements=[Element.SHOCK], name='Absorbing Messy Breakup', description='A shield that shoots at enemies and absorbs bullets'))
# char.add_equipment(Equipment(slot=Slot.CLASS_MOD, name='Showboating Red Fang', description='Gamma Burst, pet taunts and +7 grenade capacity'))
# char.add_equipment(Equipment(slot=Slot.GRENADE_MOD, elements=[Element.FIRE], name='Firestorm', description='A lot of damage but also doesnt kill me'))
char.add_equipment(Equipment(slot=Slot.ARTIFACT, name='Knife Drain White Elephant', description='Melee damage and heals on melee damage'))

# https://borderlands.fandom.com/wiki/Fish_Slap
# https://borderlands.fandom.com/wiki/Unleash_the_Dragon



# Pointy Psycho Stabber
# Redundant Face-puncher
# Brawler Ward
# Flurrying Solidary Breaker
# Unlease the Dragon
# Rain Firestorm


# 'https://www.lootlemon.com/class/amara#bad_53000531301511_4050051010000_0000000000000_0530331503030'
# 'https://www.lootlemon.com/class/amara#ead_53000531301511_5040051010000_0000000000000_0503331250031'

char = bam.add_character(vault_hunter='FL4K', descriptor='Sniper')
char.active = False





char = bam.add_character(vault_hunter='MOZE', descriptor='Boss Killer')
char.active = False





char = bam.add_character(vault_hunter='MOZE', descriptor='Iron Cub')
char.active = False





char = bam.add_character(vault_hunter='AMARA', descriptor='Big Damage')
char.active = False

bam.save_details(filepath='saveoffs/this.json')
print(json.dumps(bam.put, indent=4))




ch = CharacterHTML()

# print(ch.return_html())
ch.save_html(characters=bam.characters)


x=1




# moze - https://www.lootlemon.com/shield/revengenader-bl3
# moze - https://www.lootlemon.com/shield/razor-wire-red-suit-bl3
# zane - https://www.lootlemon.com/shield/red-card-re-charger-bl3
# zane - https://www.lootlemon.com/shield/red-card-bl3
# Amara - https://www.lootlemon.com/shield/rough-rider-bl3
# Amara - https://www.lootlemon.com/weapon/psycho-stabber-bl3


# defensive shield - https://www.lootlemon.com/shield/firewall-bl3
# defensive shield - https://www.lootlemon.com/shield/asclepius-bl3



