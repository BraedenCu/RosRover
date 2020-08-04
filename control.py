#!/usr/bin/env python3.6
import pygame
import rospy
from std_msgs.msg import Int16MultiArray, Float64MultiArray, String, Int32, Int32MultiArray, MultiArrayLayout, MultiArrayDimension
import os
import numpy as np

def publishData():

    pub_arr_key = Int32MultiArray()

    pub = rospy.Publisher('driver', Int32MultiArray, queue_size=10)

    rospy.init_node('driver', anonymous=True)

    rate = rospy.Rate(10)
    #motor speed values
    key_arr = [0,0]

    while not rospy.is_shutdown():

        x = input()

        if x=='w':
            key_arr[0] = 1
            key_arr[1] = 1
        
        elif x=='s':
            key_arr[0] = -1
            key_arr[1] = -1
        
        elif x=='a':
            key_arr[0] = 1
            key_arr[1] = -1
        
        elif x=='d':
            key_arr[0] = -1
            key_arr[1] = 1
        
        else:
            key_arr[0] = 0
            key_arr[1] = 0
            
        array_for_publishing = Int32MultiArray(data=key_arr)
        
        rospy.loginfo(array_for_publishing)

        pub.publish(array_for_publishing)


        rate.sleep()

if __name__ == '__main__':
    try:
        publishData()
    except rospy.ROSInterruptException:
        pass