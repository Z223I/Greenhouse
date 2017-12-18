from DS18B20 import DS18B20
import time


therms = DS18B20()

therms.NameDevice( "Air" )
therms.NameDevice( "Water" )

while True:
    water_temp = therms.get_current_temp( "Water" )
    print "Water temp: ", water_temp

    air_temp = therms.get_current_temp( "Air" )
    print "Air temp: ", air_temp

    print

    time.sleep(2)
