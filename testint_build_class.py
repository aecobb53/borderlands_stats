from unittest import TestCase
from unittest.mock import MagicMock, call
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


def generate_artifact():
    return Equipment(slot=Slot.ARTIFACT)

def generate_assault_rifle():
    return Equipment(slot=Slot.WEAPON)

def generate_class_mod():
    return Equipment(slot=Slot.CLASS_MOD)

def generate_grenade_mod():
    return Equipment(slot=Slot.GRENADE_MOD)

def generate_pistol():
    return Equipment(slot=Slot.WEAPON)

def generate_rocket_launcher():
    return Equipment(slot=Slot.WEAPON)

def generate_shield():
    return Equipment(slot=Slot.SHIELD)

def generate_shotgun():
    return Equipment(slot=Slot.WEAPON)

def generate_smg():
    return Equipment(slot=Slot.WEAPON)

def generate_sniper_rifle():
    return Equipment(slot=Slot.WEAPON)

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
char.add_equipment(
    Equipment(
        slot=Slot.WEAPON,
        slot_type=SlotType.ASSAULT_RIFLE,
        elements=[Element.FIRE],
        name='NoPewPew',
        description='Fast firing fire gun',
        source=EquipmentSource(link='https://www.lootlemon.com/weapon/nopewpew-bl3'),
    )
)
char.add_equipment(
    Equipment(
        slot=Slot.WEAPON,
        slot_type=SlotType.SMG,
        elements=[Element.SHOCK,
        Element.FIRE],
        name='Expert Hellshock',
        description='A solid shield dropping gun'
    )
)
char.add_equipment(
    Equipment(
        slot=Slot.WEAPON,
        slot_type=SlotType.ASSAULT_RIFLE,
        elements=[Element.ACID],
        name='Breath of the Dying',
        description='Solid Acid gun'
    )
)
char.add_equipment(
    Equipment(
        slot=Slot.WEAPON,
        slot_type=SlotType.SNIPER_RIFLE,
        elements=[Element.SHOCK],
        name='Expert Storm',
        description='Primary sniper'
    )
)
char.add_equipment(
    Equipment(
        slot=Slot.SHIELD,
        slot_type=SlotType.SHIELD,
        elements=[Element.SHOCK],
        name='Absorbing Messy Breakup',
        description='A shield that shoots at enemies and absorbs bullets'
    )
)
char.add_equipment(
    Equipment(
        slot=Slot.CLASS_MOD,
        slot_type=SlotType.CLASS_MOD,
        name='Showboating Red Fang',
        description='Gamma Burst, pet taunts and +7 grenade capacity'
    )
)
char.add_equipment(
    Equipment(
        slot=Slot.GRENADE_MOD,
        slot_type=SlotType.GRENADE_MOD,
        elements=[Element.FIRE],
        name='Firestorm',
        description='A lot of damage but also doesnt kill me'
    )
)
char.add_equipment(
    Equipment(
        slot=Slot.ARTIFACT,
        slot_type=SlotType.ARTIFACT,
        name='Rear Ender Safeguard',
        description='Creates a shield on ground slam'
    )
)

char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.SNIPER_RIFLE, elements=[Element.CRYO], name='Arctic Tamed Stalker', description='Alternative sniper'))
char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.SNIPER_RIFLE, elements=[Element.FIRE], name='Stark Krakatoa', description='Alternative sniper'))
char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.PISTOL, elements=[Element.ACID], name='Venomous Hornet', description='An alternative to the Breat of the Dying'))
char.archived_slots.append(Equipment(slot=Slot.WEAPON, slot_type=SlotType.ASSAULT_RIFLE, elements=[Element.FIRE], name='NoPewPew', description='Fast firing fire gun'))

# # For testing only
# char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.SMG, elements=[Element.CRYO, Element.RADIATION], name='Binary Superflous Devoted', description='Nothing Special')
# # print(json.dumps(char.put, indent=4))
# # x=1


char = bam.add_character(vault_hunter='MOZE', descriptor='MAIN Nuke Build')
char.active_build = BuildLink(url='https://www.lootlemon.com/class/moze#xxxx_0000000000000_5350553050151_0150000000000_3353001541001')
char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.ASSAULT_RIFLE, elements=[Element.FIRE], name='NoPewPew', description='Fast firing fire gun'))
char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.ASSAULT_RIFLE, elements=[Element.RADIATION], name='Double-Penetrating Gross Bearcat', description='Grenade gun for shields'))
char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.ASSAULT_RIFLE, elements=[Element.CRYO], name='Double-Penetrating Gross Bearcat', description='Grenade gun for armor'))
char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.ROCKET_LAUNCHER, elements=[Element.KENETIC], name='Tunguska', description='Large AOE damager'))
char.add_equipment(Equipment(slot=Slot.SHIELD, slot_type=SlotType.SHIELD, elements=[Element.FIRE], name='Bloated Front Loader', description='Reduces action skill cooldown'))
char.add_equipment(Equipment(slot=Slot.CLASS_MOD, slot_type=SlotType.CLASS_MOD, name='Growling Reinforced Bear Trooper', description='Build centered class mod'))
char.add_equipment(Equipment(slot=Slot.GRENADE_MOD, slot_type=SlotType.GRENADE_MOD, name='Tran-fusion Tracker', description='Healing grenade'))
char.add_equipment(Equipment(slot=Slot.ARTIFACT, slot_type=SlotType.ARTIFACT, name='Ravaging Last Stand', description='Nothing special. Eventually find a new one'))


char = bam.add_character(vault_hunter='ZANE', descriptor='MAIN Speedy Boy')
char.active_build = BuildLink(url='https://www.lootlemon.com/class/zane#xxxxxx_00000000000000_50551015501_50030500000000_500135155301')
char.archived_builds = [
    BuildLink(url='https://www.lootlemon.com/class/zane#xxxxxx_50553011513131_55551015531_00000000000000_000000000000'),
    BuildLink(url='https://www.lootlemon.com/class/zane#aabdtr_50000000000000_55551515501_00000000000000_500135105331'),
]
char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.SHOTGUN, elements=[Element.FIRE], name='Speedloadn Hellwalker', description='Shotgun with high damange'))
char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.PISTOL, elements=[Element.RADIATION], name='Nuclear Infinity', description='A shield gun that never reloads'))
char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.SMG, elements=[Element.CRYO, Element.RADIATION], name='Binary Superflous Devoted', description='Nothing Special'))
char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.SHOTGUN, elements=[Element.SHOCK], name='The Lab', description='Shotgun with high damange'))
char.add_equipment(Equipment(slot=Slot.SHIELD, slot_type=SlotType.SHIELD, elements=[Element.FIRE], name='Snap-Shot Whiskey Tango Foxtrot', description='Shotgun with high damange'))
char.add_equipment(Equipment(slot=Slot.CLASS_MOD, slot_type=SlotType.CLASS_MOD, name='Shockwave Smashing Antifreeze', description='increased damage while sliding or in the air'))
char.add_equipment(Equipment(slot=Slot.GRENADE_MOD, slot_type=SlotType.GRENADE_MOD, name='Tinas Hippity Hopper', description='Just an unused grenade'))
char.add_equipment(Equipment(slot=Slot.ARTIFACT, slot_type=SlotType.ARTIFACT, name='Hasty Snowdrift', description='A more useful snowdrift but this is awesome'))


char = bam.add_character(vault_hunter='AMARA', descriptor='MAIN Melee Build')
char.active_build = BuildLink(url='https://www.lootlemon.com/class/amara#efd_53000531300501_5050051033031_5000100000000_0500331000000')
char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.SHOTGUN, elements=[Element.FIRE], name='Speedloadn Hellwalker', description='Shotgun with high damange'))
char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.SMG, elements=[Element.SHOCK, Element.FIRE], name='Expert Hellshock', description='A solid shield dropping gun'))
char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.PISTOL, elements=[Element.ACID], name='Venomous Hornet', description='An alternative to the Breat of the Dying'))
char.add_equipment(Equipment(slot=Slot.WEAPON, slot_type=SlotType.ASSAULT_RIFLE, elements=[Element.KENETIC], name='Blade Fury', description='Shoots melee damage'))
# char.add_equipment(Equipment(slot=Slot.SHIELD, slot_type=SlotType.SHIELD, elements=[Element.SHOCK], name='Absorbing Messy Breakup', description='A shield that shoots at enemies and absorbs bullets'))
# char.add_equipment(Equipment(slot=Slot.CLASS_MOD, slot_type=SlotType.CLASS_MOD, name='Showboating Red Fang', description='Gamma Burst, pet taunts and +7 grenade capacity'))
# char.add_equipment(Equipment(slot=Slot.GRENADE_MOD, slot_type=SlotType.GRENADE_MOD, elements=[Element.FIRE], name='Firestorm', description='A lot of damage but also doesnt kill me'))
char.add_equipment(Equipment(slot=Slot.ARTIFACT, slot_type=SlotType.ARTIFACT, name='Knife Drain White Elephant', description='Melee damage and heals on melee damage'))

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
# print(json.dumps(bam.put, indent=4))




ch = CharacterHTML()

# print(ch.return_html())
ch.save_html(characters=bam.characters)


er = EquipmentReview()
er.load_data()

results = er.find_equipment(
    slot=Slot.SHIELD,
    slot_type=[SlotType.SINGULARITY, SlotType.BOOSTER],
    equipment_source=[
        EquipmentSource(content='Anshin')
    ]
)
# er.open_equipment_urls(
#     slot=Slot.SHIELD,
# )

es1 = EquipmentSource(content='one', mob='one')
es2 = EquipmentSource(mob='two', link='two')
es1.update(es2)

eq1 = Equipment(slot=Slot.EMPTY, notes=['one'], elements=[Element.FIRE])
eq1.lock()
eq2 = Equipment(slot=Slot.WEAPON, notes=['two'], description='two')
# eq1.update(eq2)
a = eq1.notes
eq1.update(eq2)
b = eq1.notes

eq1.unlock()
eq1.update(eq2)
c = eq1.notes

ugh = datetime(2020, 1, 1)
cle = ChangeLogEntry(note='test')
this = cle.put
tha = ChangeLogEntry.build(this)


er.save_details()
data = er.load_details()



opened_equipment = er.open_equipment_urls(
    slot=Slot.SHIELD,
    reviewed=False,
    count=10,
)

reviewed_mark = False

updated_names = {e.name: e.slot for e in opened_equipment}
x=1
for name, slot in updated_names.items():
    equipment = er.find_equipment(
        name=name,
        slot=slot,
    )[0]
    equipment.reviewed = reviewed_mark

if updated_names:
    er.save_details()


x=1

'''
usefulness on a scale 1-10
Notable numbers 
    1 ignore
    3 doesnt seem useful
    5 interesting
    7 Useful for a build but nothing im looking at now
    9 useful for a build i want probably
    10 have to have 

The shields without links were marked as reviewed but were never looked at. Go back at some point

3 All-in
5 Asclepius - Could be rally tanky with health regen when taking shield damange
5 Back Ham - very tanky
5 Band of Sitorak - extra health
7 Beskar - reflects 50% of incoming shots
7 Big Boom Blaster - drops shield charges that also restore grenands and launcher amo
5 Black Hole - pull enemies in when shield breaks
1 Double Downer - extra FFYL time and damage
3 Ember's Blaze - constantly deals fire damage to everybody around
3 Bullet Buffet Faulty Star - chance to nova when damaged
7 Firewall - Bounces back some shots when crouched
7 Front Loader - lower health but higher shields
5 Frozen Heart - Cryo nova when depleted and heals for damage done
3 Gas Mask - extra FFYL time
3 Golden Touch - good utility shield for leveling
3 Reposte Impaler - launches homing missles when shield breaks
5 Infernal Wish - A lot of fire damage. Probably best on a sniper
8 Initiative - No shield but increases damage reload and health
10 Limit Break - absorb projectile and increase cooldown rate and increases health i think it would be good on Amara
9 Loop of 4n631 - when depleted doubles cooldown rate
7 MSRC Auto-Dispensary - A fun shield that alters stats as you pick up shield charges
5 Equalizer Madcap - Very high shield capacity but halfs FFYL time
3 Mendel's Multivitiamin Shield - Increases health and health regen
5 Messy Breakup - Really funny, shoots at enemies, gets annoying after a while
5 MoXXi's Embrace - Heals self and allies when shield breaks
5 Mr Caffeine - faster fire rate and reload if shield is full
5 Nova Berner - Triggers fire nova on shield break and fill
5 Old God - extra shield damage and shock resistance
8 Plus Ultra - Absorb shots, drops charges that improves cooldown 
5 Re-Charger Berner - Elemental nova on shield break and fill and fully fill shield again
5 Re-Charger - fully fill shield on shield break
9 Re-Router - Draines 50% of shield to do +120% damage and heals flat amount. Very useful for sniper build
9 Re-Volter - On break increases fire rate and shock damage
8 Rectifier - Constantly deals shock damage to nearby enemies, Would only be useful for a Moze build if that
5 Red Card - Sliding into enemy breaks shield and does what shield was broken as damag
7 Red Card Re-Charger - Sliding into enemy breaks shield and does what shield was broken as damage, fully recharges shield, Could be useful on Zane
8 Red Suit - Constantly deals radiation damage, would only be useful on Moze
10 Revengenader - Drops grenade if shield breaks, would be very useful on Zane
8 Rico - Reflect bullets frequently, could be useful on Fl4k for survivability
8 Rough Rider - lower damage taken and more health but no shield capacity, adds melee damage and speed
8 Scream of Terror - health regen, shield break can cause enemies to attack eachother for a shot bit of time, could be useful on zane
8 Shooting Star - When shield broken melee hits cause explosions, could be useful on Amara
5 Version 0.m - extra damage on first shot and drops an extra damage spot on floor if shield breaks
5 Snowshoe - sliding damages and breaks shield
5 Stinger - Extra melee damage if shield is full
7 Stop-Gap - Immune to damage imediatly after shield break, very tanky
5 The Transformer - All shock damage recharges shield instead and absorbs bullets
5 Torch - On shield break send out balls of fire
8 Unpaler - A lot of extra melee damage when shield is broken
5 Void Rift - Cryo homing rockets and cryo nova on break
5 Ward - Health regen or extra damage when shield is full or depleted
7 Wattson - Explodes after taking damage, could be useful on Moze or close builds
5 Whiskey Tango Foxtrot - 3 IEDs after being hit








'''

# moze - https://www.lootlemon.com/shield/revengenader-bl3
# moze - https://www.lootlemon.com/shield/razor-wire-red-suit-bl3
# zane - https://www.lootlemon.com/shield/red-card-re-charger-bl3
# zane - https://www.lootlemon.com/shield/red-card-bl3
# Amara - https://www.lootlemon.com/shield/rough-rider-bl3
# Amara - https://www.lootlemon.com/weapon/psycho-stabber-bl3


# defensive shield - https://www.lootlemon.com/shield/firewall-bl3
# defensive shield - https://www.lootlemon.com/shield/asclepius-bl3



