#/usr/bin/python2.7



# TODO: and code for keyboard interupt.
# On keyboard interrupt... global GPIO not defined.

#import sys
#sys.path.append('/home/pi/pythondev/Greenhouse')


from DS18B20 import DS18B20
import time
import os
from relaypipy import RelayPiPy
from Heater import Heater
#from FishFeeder2.fishfeeder2 import FishFeeder2

pinList = []


def writeStats(_airTemp, _waterTemp, _heaterStatus):
    with open("stats.csv", "a") as log:
        log.write( "{0}, ".format( time.strftime("%Y-%m-%d %H:%M:%S") ) )
        log.write( "{0}, ".format( str(_airTemp) ) )
        log.write( "{0}, ".format( str(_waterTemp) ) )
        log.write( "{0} \n".format( str(_heaterStatus) ) )





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

    fMinAirTemp = float( raw_input('Minimum air temp: ') )
    fMinWaterTemp = float( raw_input('Minimum water temp: ') )

    gh_heater = Heater( heaterRelay, fMinAirTemp, fMinWaterTemp )

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

#from pathlib import Path
#stat_file = Path("stats.csv")
#if stat_file.is_file():
#    os.remove(stat_file)

try:
    os.remove("stats.csv")
except:
    print


try:

    relay_init()
    print "Done with relay."




    # create and initialize fish feeder.
    # TODO: Update these to the correct pin numbers.
#    gh_fishfeeder = FishFeeder2(1, 1, 1, 1)


    print "Heater initialization..."
    lgh_heater = heater_init()


    timeDelayMinutes = float( raw_input('Time between reading (minutes): ') )



    therms = DS18B20()

    therms.NameDevice( "Air" )
    therms.NameDevice( "Water" )
    therms.create_dict()

    while True:
        air_temp = therms.get_current_temp( "Air" )
        fair_temp = float( air_temp )
        print "Air temp: ", fair_temp

        water_temp = therms.get_current_temp( "Water" )
        fwater_temp = float( water_temp )
        print "Water temp: ", fwater_temp


        heaterOn = lgh_heater.run(fair_temp, fwater_temp)

        if heaterOn:
            heaterStatus = 80
            print "HEAT"
        else:
            heaterStatus = 30
            print "temps ok"

        writeStats(fair_temp, fwater_temp, heaterStatus)

        print

        time.sleep(timeDelayMinutes * 60)

# End try

except KeyboardInterrupt:
    print "Keyboard Interrupt"
# End except

shutdown()
