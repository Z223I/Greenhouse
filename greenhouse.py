from DS18B20 import DS18B20
import time
from relaypipy import RelayPiPy
import Heater

gh_relay = RelayPiPy()

# Initialize list with pin numbers
pinList = [ 6, 13, 19, 26 ]

gh_relay.init(pinList)

# Reserve relays 0, 1, 2 for fish feeder
powerRelay = 0
terminal1Relay = 1
terminal2Relay = 2

# create and initialize fish feeder.



# create heater.
heaterRelay = 3
heaterPin = pinList[ heaterRelay ]

gh_heater = Heater( heaterPin )

gh_heater.init()

gh_heater.off()



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
