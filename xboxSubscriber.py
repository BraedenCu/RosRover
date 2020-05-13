#!/usr/bin/env python3.6
import rospy
import rospy
from std_msgs.msg import String,Int32,Int32MultiArray,MultiArrayLayout,MultiArrayDimension, Int16MultiArray
from rosroverxbox.msg import IntList
from adafruit_servokit import ServoKit

def init():
    global kit
    kit = ServoKit(channels=16)

def callbackButtons(data):
    #runs everytime button changes
    arr = data.data
    array = [x for x in arr]
    if array[0] > 0.8:
        kit.servo[1].angle=180
    else:
        kit.servo[1].angle=0
    print(array[0])

def callbackAxis(data):
    #runs everytime axis changes, the below is a placeholder
    x = 1

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('axis', IntList, callbackAxis)

    rospy.Subscriber('buttons', IntList, callbackButtons)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        init()
        listener()
    except rospy.ROSInterruptException:
        pass
