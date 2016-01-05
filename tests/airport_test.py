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

    def test_instruct_to_take_off_removes_plane_from_planes(self):
        self.airport.instruct_to_land(self.plane)
        self.airport.instruct_to_take_off(self.plane)
        self.assertNotIn(self.plane, self.airport.planes)

    def test_instruct_to_take_off_calls_take_off_on_plane(self):
        self.airport.instruct_to_land(self.plane)
        self.airport.instruct_to_take_off(self.plane)
        self.plane.take_off.assert_called_with()

    def test_instruct_to_take_off_should_fail_if_plane_not_at_airport(self):
        with self.assertRaisesRegexp(Exception, 'Plane is not at this airport'):
            self.airport.instruct_to_take_off(self.plane)
