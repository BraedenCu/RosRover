#!/usr/bin/env python3.6
import rospy
import rospy
from std_msgs.msg import String,Int32,Int32MultiArray,MultiArrayLayout,MultiArrayDimension, Int16MultiArray
#rosroverxbox is the name of the package, and IntList is the name of the .msg file
from rosroverxbox.msg import IntList
from adafruit_motorkit import MotorKit

def init():
    global kit
    kit = MotorKit()

def callbackButtons(data):
    #runs everytime button changes
    pass

def callbackAxis(data):
    #runs everytime axis changes
    deadzone = 0.1
    if data[1] >= deadzone:
        kit.motor1.throttle = data[1]
    if data[3] >= deadzone:
        kit.motor2.throttle = data[3]
    else:
        kit.motor1.throttle = 0
        kit.motor2.throttle = 0


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
