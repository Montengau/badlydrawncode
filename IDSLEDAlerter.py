#!/usr/bin/python3

# install this script inside the /var/log/suricata directory, and set the script to be run every minute via a cronjob 

import RPi.GPIO as g
from time import sleep

g.setmode(g.BCM)
g.setup([18,23,21],g.OUT)

def flashLED(gpioPin):
    g.output(gpioPin,1)
    sleep(0.5)
    g.output(gpioPin,0)
    sleep(0.5)

while True:
    with open("fast.log") as f:
        last_row = f.readlines()[-1]

        # do stuff to light LEDs depending on record read

        if "[Priority: 2]" in last_row:
            flashLED(18)
        elif "[Priority: 3]" in last_row:
            flashLED(23)
        elif "[Priority: 1]" in last_row:
            flashLED(21)s
