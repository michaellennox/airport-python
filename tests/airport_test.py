import unittest
from mock import Mock
from app.airport import Airport

class TestAirport(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()
        self.plane = Mock()

    def test_airport_initializes_with_empty_planes_array(self):
        self.assertEqual(self.airport.planes, [])

    def test_instruct_to_land_sockets_plane_in_planes(self):
        self.airport.instruct_to_land(self.plane)
        self.assertIn(self.plane, self.airport.planes)

    def test_instruct_to_land_calls_land_on_plane(self):
        self.airport.instruct_to_land(self.plane)
        self.plane.land.assert_called_with()
