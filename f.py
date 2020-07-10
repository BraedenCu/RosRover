#!/usr/bin/env python3.6
import rospy
import rospy
from std_msgs.msg import String,Int32,Int32MultiArray,MultiArrayLayout,MultiArrayDimension, Int16MultiArray
#rosroverxbox is the name of the package, and IntList is the name of the .msg file
from cleaningbot.msg import IntList
from adafruit_motorkit import MotorKit

def init():
    pass
    global kit
    kit = MotorKit()

def callback0(data):
    #runs everytime button changes
    arr = data.drive
    if arr[0] != 0:
        kit.motor1.throttle=arr[1]
    if arr[1] != 0:
        kit.motor1.throttle=arr[0]
    else:
        kit.motor1.throttle = 0
        kit.motor2.throttle = 0


def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("driver", IntList, callback0)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        init()
        listener()
    except rospy.ROSInterruptException:
        kit.motor1.throttle = 0
        kit.motor2.throttle = 0
