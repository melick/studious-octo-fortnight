import pyowm
import constants

owm = pyowm.OWM(constants.DEFAULT_API_KEY)


def owm_status():
    '''Return Open Weather Map API status (http://openweathermap.org/)'''
    online = owm.is_API_online()
    return online


def owm_observation(city_id):
    '''Return an Observation object in variable observation''' 
    observation = owm.weather_at_id(city_id)
    return observation


def owm_w(city_id):
    '''Return just the weather data from the object'''
    w = owm.weather_at_id(city_id).get_weather()
    return w


def owm_time(city_id):
    '''Return reading time'''
    t = owm.weather_at_id(city_id).get_weather().get_reference_time(timeformat='iso')
    time = t[:19]
    return time


def owm_speed(city_id):
    '''Return current wind speed'''
    speed = owm.weather_at_id(city_id).get_weather().get_wind()['speed']
    return speed


def owm_direction(city_id):
    '''Return current wind direction in degrees'''
    direction = owm.weather_at_id(city_id).get_weather().get_wind()['deg']
    return direction


def owm_pressure(city_id):
    '''Return current barometric pressure'''
    pressure = owm.weather_at_id(city_id).get_weather().get_pressure()['press']
    return pressure


def owm_temperature(city_id):
    '''Return current temperature in Fahrenheit degrees'''
    temperature = owm.weather_at_id(city_id).get_weather().get_temperature('fahrenheit')['temp']
    return temperature


def owm_humidity(city_id):
    '''Return current humidity'''
    humidity = owm.weather_at_id(city_id).get_weather().get_humidity()
    return humidity

