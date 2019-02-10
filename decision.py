#THESEUS 2019
#Decision making module

#LCM
import lcm

#TODO specific lcm type import statements (world model)

#Camera
from picamera import PiCamera
from time import sleep

#RGB
import time
import board
import busio
import adafruit_tcs34725
import serial

#Big noise
import RPi.GPIO as GPIO
import sound

# returns 0 if continuing straight, 1 if should turn left, 2 if should turn right
# if turning, will also return a non-zero value of intensity
def choose_direction(world_state, centerline):
    left_on_line = on_line(world_state.LEFT[0], world_state.LEFT[1], world_state.LEFT[2])
    center_on_line = on_line(world_state.CENTER[0], world_state.CENTER[1], world_state.CENTER[2])
    right_on_line = on_line(world_state.RIGHT[0], world_state.RIGHT[1], world_state.RIGHT[2])
    if left_on_line:
        if centerline == False:
            if center_on_line:
                # if center sensor is also on line, we have reached an intersection
                # decide to turn/go straight
            else:
                return (0, 0)
        else:
            if center_on_line:
                #we have reached an intersection, determine what to do

    elif center_on_line:
        if centerline == True:
            return (0, 0)
        else:
            return (2, .25)
    else:
        if centerline == True:
            return (2, .25)
        else:
            return (1, .25)





