import unittest
from constants import place_name
from functions import owm
from functions import owm_status
from functions import owm_observation
from functions import owm_w
from functions import owm_time
from functions import owm_speed
from functions import owm_direction
from functions import owm_pressure
from functions import owm_temperature
from functions import owm_humidity


class TestCases(unittest.TestCase):

    def setUp(self):
        pass

    def test_online(self):
        '''Open Weather Maps API should report being online'''
        self.online = owm_status()
        self.assertEqual(self.online, 1)

#    def test_time(self):
#        '''check time function'''
#        self.time = owm_time(place_name)
#        self.assertEqual(self.time, 1)

    def test_speed(self):
        '''
        check speed, should be less than 150
        unless we are having a hurricane or tornado
        '''
        self.speed = owm_speed(place_name)
        self.assertLess(self.speed, 150)

    def test_direction(self):
        '''check direction, should be less than or equal to 359'''
        self.direction = owm_direction(place_name)
        self.assertLessEqual(self.direction, 359)

    def test_pressure(self):
        '''
        check barometric pressure, should be
        greater than or equal to 910 unless
        '''
        self.pressure = owm_pressure(place_name)
        self.assertGreaterEqual(self.pressure, 910)

    def test_temperature(self):
        '''check temperature, should be less than or equal to 120'''
        self.temperature = owm_temperature(place_name)
        self.assertLessEqual(self.temperature, 120)

    def test_humidity(self):
        '''check humidity, should be less than or equal to 100'''
        self.humidity = owm_humidity(place_name)
        self.assertLessEqual(self.humidity, 100)


if __name__ == '__main__':
    unittest.main()
