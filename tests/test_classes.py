from unittest import TestCase
from unittest.mock import MagicMock, call

import json

from classes import (
    Element,
    Equipment,
    Slot,
    VaultHunter,
    Character,
    BorderlandsAccountManager,
)

class BuildTest(TestCase):
    def add_equipment(self):
        bam = BorderlandsAccountManager()
        assert bam.put == []
        bam.add_character(vault_hunter='moze', descriptor='Nuke Build')
        char = bam.find_characters(vault_hunter='moze')[0]
        char.add_equipment(equipment=generate_artifact())
        char.add_equipment(equipment=generate_assault_rifle())
        char.add_equipment(equipment=generate_class_mod())
        char.add_equipment(equipment=generate_grenade_mod())
        char.add_equipment(equipment=generate_pistol())
        char.add_equipment(equipment=generate_rocket_launcher())
        char.add_equipment(equipment=generate_shield())
        char.add_equipment(equipment=generate_shotgun())
        char.add_equipment(equipment=generate_smg())
        char.add_equipment(equipment=generate_sniper_rifle())
        char.add_equipment(equipment=generate_None())
        equip = generate_artifact()
        equip.description = 'Associate only'
        char.add_associate(equipment=equip)
        equip = generate_artifact()
        equip.description = 'Archive only'
        char.add_archive(equipment=equip)
        char.add_archive(equipment=generate_None())

        print(json.dumps(bam.put, indent=4))
        a = bam.put
        bam.save_details(filepath='saveoffs/this.json')
        bam2 = bam.load_details(filepath='saveoffs/this.json')
        # print(json.dumps(bam2.put, indent=4))


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


bam = BorderlandsAccountManager()
x=1
print(json.dumps(bam.put, indent=4))
x=1
bam.add_character(vault_hunter='moze', descriptor='Nuke Build')
a = bam.find_characters(vault_hunter='moze')[0]
a.add_equipment(equipment=generate_artifact())
a.add_equipment(equipment=generate_assault_rifle())
a.add_equipment(equipment=generate_class_mod())
a.add_equipment(equipment=generate_grenade_mod())
a.add_equipment(equipment=generate_pistol())
a.add_equipment(equipment=generate_rocket_launcher())
a.add_equipment(equipment=generate_shield())
a.add_equipment(equipment=generate_shotgun())
a.add_equipment(equipment=generate_smg())
a.add_equipment(equipment=generate_sniper_rifle())
a.add_equipment(equipment=generate_None())

equip = generate_artifact()
equip.description = 'Associate only'
a.add_associate(equipment=equip)
equip = generate_artifact()
equip.description = 'Archive only'
a.add_archive(equipment=equip)
a.add_archive(equipment=generate_None())

x=1
print(json.dumps(bam.put, indent=4))
x=1
bam.save_details(filepath='saveoffs/this.json')
bam2 = bam.load_details(filepath='saveoffs/this.json')
print(json.dumps(bam2.put, indent=4))
x=1



# b = Build(
#     vault_hunter=BorderlandsClasses.MOZE,
#     build_description='Nuke build'
# )

# # b.add_active(slot='artifact', name='test')
# # b.add_active(slot='assault', name='test')
# # b.add_active(slot=Slot.ASSAULT_RIFLE, name='test')
# # b.add_active(slot='assault', elements=[Element.FIRE], name='test')
# # b.add_active(slot='assault', elements=['fire'], name='test')
# # b.add_associated(slot='assault', elements=['fire'], name='test')

# b.add_active(slot='artifact', name='test')
# b.add_active(slot='assault_rifle', name='test')
# b.add_active(slot='class_mod', name='test')
# b.add_active(slot='grenade_mod', name='test')
# b.add_active(slot='pistol', name='test')
# b.add_active(slot='rocket_launcher', name='test')
# b.add_active(slot='shield', name='test')
# b.add_active(slot='shotgun', name='test')
# b.add_active(slot='smg', name='test')
# b.add_active(slot='sniper_rifle', name='test')

# # a1 = b.create_equipment(slot='artifact', name='test')
# # a2 = b.create_equipment(slot='assault', name='test')

# # b1 = b.guns
# # b2 = b.fire_guns
# # b3 = b.assault_rifles
# # b4 = b.kenetic_guns
# # # b5 = b.find_artifacts(collection='active')

# # x=1

# # print(json.dumps(b.put, indent=4))
# # print(json.dumps(b.full_put(), indent=4))
# # fl = 'saveoffs/this.json'
# # print(json.dumps(b.save_data(filepath=fl), indent=4))
# # print(b.load_data(filepath=fl))

# bam = BorderlandsAccountManager()
# x=1
# print(json.dumps(bam.put, indent=4))
# x=1
# bam.add_character('fl4k', 'NonNuke Build')
# # bam.add_character('moze', 'that build')
# # c1 = bam.find_characters('moze')

# print(json.dumps(bam.put, indent=4))

x=1

