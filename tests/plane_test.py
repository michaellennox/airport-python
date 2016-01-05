import unittest
from app.plane import Plane

class TestPlane(unittest.TestCase):

    def setUp(self):
        self.plane = Plane()

    def test_isflying_should_be_true_on_initialization(self):
        self.assertTrue(self.plane.isflying)

    def test_land_should_change_is_flying_to_false(self):
        self.plane.land()
        self.assertFalse(self.plane.isflying)
