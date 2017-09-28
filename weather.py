import pyowm
import constants
from constants import place_name
import functions
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
import csv
from time import gmtime, strftime


'''check Open Weather Map API status'''
stat = owm_status()

if stat:
    '''the API was online, get readings'''
    x = owm_time(place_name)
    s = owm_speed(place_name)
    d = owm_direction(place_name)
    p = owm_pressure(place_name)
    t = owm_temperature(place_name)
    h = owm_humidity(place_name)
    ts = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    '''Open output file in apend mode, write data'''
    with open('datafile.csv', 'a') as datafile:
        csvwriter = csv.writer(datafile, delimiter=',', dialect='excel',
                               quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        csvwriter.writerow([x, s, d, p, t, h, ts])

else:
    '''the API was online'''
    print "OWM was offline (%s)" % (online)


'''put your toys away, little Johnny'''
datafile.close()


'''HC SVNT DRACONES'''
