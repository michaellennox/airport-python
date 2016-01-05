import unittest
from app.airport import Airport
from app.plane import Plane

class TestUserStory(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()
        self.plane = Plane()

    def test_instructing_a_plane_to_land_should_land_it(self):
        # As an air traffic controller
        # So I can get passengers to a destination
        # I want to instruct a plane to land at an airport and confirm that it has landed
        self.airport.instruct_to_land(self.plane)
        self.assertIn(self.plane, self.airport.planes)
        self.assertFalse(self.plane.isflying)
