#!/usr/bin/env python3.6
import rospy
import rospy
from std_msgs.msg import String,Int32,Int32MultiArray,MultiArrayLayout,MultiArrayDimension, Int16MultiArray
from rosroverxbox.msg import IntList

def callbackButtons(data):
    #rospy.loginfo(rospy.get_caller_id() + "Button vals: %s", data)
    print(data)

def callbackAxis(data):
    #rospy.loginfo(rospy.get_caller_id() + "Axis Vals: %s", data)
    print(data)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('axis', IntList, callbackAxis)

    rospy.Subscriber('buttons', IntList, callbackButtons)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
