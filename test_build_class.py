from unittest import TestCase
from unittest.mock import MagicMock, call

from classes import (
    Element,
    Slot,
    Equipment,
    Build,
)

class BuildTest(TestCase):
    def add_equipment(self):
        b = Build()


b = Build()

b.add_active(slot='assault', name='test')
b.add_active(slot=Slot.ASSAULT_RIFLE, name='test')
b.add_active(slot='assault', elements=[Element.FIRE], name='test')
b.add_active(slot='assault', elements=['fire'], name='test')

a1 = b.create_equipment(slot='artifact', name='test')
a2 = b.create_equipment(slot='assault', name='test')

b1 = b.guns()

x=1

