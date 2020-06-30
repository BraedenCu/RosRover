#!/usr/bin/env python3.6
import pygame
import rospy
from std_msgs.msg import Int16MultiArray, Float64MultiArray, String, Int32, Int32MultiArray, MultiArrayLayout, MultiArrayDimension
import os
import numpy as np
#rosroverxbox is the name of the package, and IntList is the name of the .msg file
from rosroverxbox.msg import IntList

def setup():
    #I don't want pygame to display anything, so simply creating a "dummy" server for pygame to display on
    os.environ["SDL_VIDEODRIVER"] = "dummy"
    pygame.display.init()
    pygame.joystick.init()
    pygame.joystick.Joystick(0).init()
    # Prints the joystick's names
    JoyName = pygame.joystick.Joystick(0).get_name()
    print("Name of the joystick:")
    print(JoyName)
    # Gets the number of axes
    JoyAx = pygame.joystick.Joystick(0).get_numaxes()
    print("Number of axis:")
    print(JoyAx)

def publishData():

    pub_arr_joy = IntList()
    pub_arr_butt = IntList()

    axis = rospy.Publisher('axis', IntList, queue_size=10)
    buttons = rospy.Publisher('buttons', IntList, queue_size=10)
    rospy.init_node('controller', anonymous=True)
    rate = rospy.Rate(10)
    joystick_arr = [0, 0, 0, 0]
    buttons_arr = [0, 0, 0, 0]


    while not rospy.is_shutdown():

        pygame.event.pump()

        rightX = pygame.joystick.Joystick(0).get_axis(0)
        rightY = pygame.joystick.Joystick(0).get_axis(1)
        leftX = pygame.joystick.Joystick(0).get_axis(2)
        leftY = pygame.joystick.Joystick(0).get_axis(3)

        joystick_arr[0] = rightX
        joystick_arr[1] = rightY
        joystick_arr[2] = leftX
        joystick_arr[3] = leftY

        if pygame.joystick.Joystick(0).get_button(0):
            buttons_arr[0] = 1
        
        elif pygame.joystick.Joystick(0).get_button(1):
            buttons_arr[1] = 1
        
        elif pygame.joystick.Joystick(0).get_button(2):
            buttons_arr[2] = 1
        
        elif pygame.joystick.Joystick(0).get_button(3):
            buttons_arr[3] = 1
        
        else:
            buttons_arr[0] = 0
            buttons_arr[1] = 0
            buttons_arr[2] = 0
            buttons_arr[3] = 0
        
        #publish data array
        pub_arr_butt = [int(x) for x in buttons_arr]
        pub_arr_joy = [int(x) for x in joystick_arr]
        #rospy.loginfo(buttonsarr)
        #rospy.loginfo(joystick_arr)
        axis.publish(pub_arr_joy)
        buttons.publish(buttons_arr)

        rate.sleep()

if __name__ == '__main__':
    try:
        setup()
        publishData()
    except rospy.ROSInterruptException:
        pass
    
