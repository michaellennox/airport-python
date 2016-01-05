import unittest
from app.plane import Plane

class TestPlane(unittest.TestCase):

    def setUp(self):
        self.plane = Plane()

    def test_isflying_should_be_true_on_initialization(self):
        self.assertTrue(self.plane.isflying)

    def test_land_should_change_isflying_to_false(self):
        self.plane.land()
        self.assertFalse(self.plane.isflying)

    def test_take_off_should_change_isflying_to_true(self):
        self.plane.land()
        self.plane.take_off()
        self.assertTrue(self.plane.isflying)

    def test_take_off_should_fail_if_plane_not_landed(self):
        with self.assertRaisesRegexp(Exception, 'Plane cannot take off while flying'):
            self.plane.take_off()
