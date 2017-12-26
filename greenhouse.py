#/usr/bin/python2.7



# TODO: and code for keyboard interupt.
# On keyboard interrupt... global GPIO not defined.

import DS18B20
import time
import RelayPiPy
import Heater
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
#    heaterPin = pinList[ heaterRelay ]

    gh_heater = Heater( heaterRelay )

#    gh_heater.init()

    gh_heater.off()
    time.sleep(2)

    gh_heater.off()
    time.sleep(2)

    return gh_heater


##################################################
# Function shutdown
##################################################

def shutdown():
    #GPIO.cleanup()
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


#    print "Heater initialization..."
#    gh_heater = Heater()
    lgh_heater = heater_init()






    therms = DS18B20()

    therms.NameDevice( "Air" )
    therms.NameDevice( "Water" )
    therms.create_dict()

    while True:
        water_temp = therms.get_current_temp( "Water" )
        print "Water temp: ", water_temp

        air_temp = therms.get_current_temp( "Air" )
        print "Air temp: ", air_temp

        print

        time.sleep(2)

# End try

except KeyboardInterrupt:
    print "Keyboard Interrupt"
# End except

shutdown()
