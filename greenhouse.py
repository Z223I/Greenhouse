#/usr/bin/python2.7



# TODO: and code for keyboard interupt.
# On keyboard interrupt... global GPIO not defined.

import sys
sys.path.append('/home/pi/pythondev/Greenhouse')


from DS18B20 import DS18B20
import time
from relaypipy import RelayPiPy
from Heater import Heater
#from FishFeeder2.fishfeeder2 import FishFeeder2

pinList = []

def relay_init():
    global pinList

    gh_relay = RelayPiPy()

    # Initialize relay list with pin numbers
    pinList = [ 6, 13, 19, 26 ]

    gh_relay.init(pinList)

    # Reserve relays 0, 1, 2 for fish feeder
    powerRelay = 0
    terminal1Relay = 1
    terminal2Relay = 2

    # Reserve relay 3 for heater



def heater_init():
    global pinList


    # create heater.
    heaterRelay = 3

    gh_heater = Heater( heaterRelay )

#    gh_heater.on()
#    time.sleep(2)

#    gh_heater.off()
#    time.sleep(2)

    return gh_heater


##################################################
# Function shutdown
##################################################

def shutdown():
#    GPIO.cleanup()
    print
    print "Bye!"

# End shutdown




##################################################
#
# Main
#
##################################################


try:
    relay_init()
    print "Done with relay."




    # create and initialize fish feeder.
    # TODO: Update these to the correct pin numbers.
#    gh_fishfeeder = FishFeeder2(1, 1, 1, 1)


    print "Heater initialization..."
    lgh_heater = heater_init()








    therms = DS18B20()

    therms.NameDevice( "Air" )
    therms.NameDevice( "Water" )
    therms.create_dict()

    while True:
        water_temp = therms.get_current_temp( "Water" )
        fwater_temp = float( water_temp )
        print "Water temp: ", water_temp, fwater_temp

        air_temp = therms.get_current_temp( "Air" )
        fair_temp = float( air_temp )
        print "Air temp: ", air_temp, fair_temp

        print

        time.sleep(2)

# End try

except KeyboardInterrupt:
    print "Keyboard Interrupt"
# End except

shutdown()
