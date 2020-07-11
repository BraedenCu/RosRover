#!/usr/bin/env python3.6
import rospy
import rospy
from std_msgs.msg import String,Int32,Int32MultiArray,MultiArrayLayout,MultiArrayDimension, Int16MultiArray
#rosroverxbox is the name of the package, and IntList is the name of the .msg file
from cleaningbot.msg import IntList
import RPi.GPIO as GPIO          
from time import sleep

def init():
    
    global in1 = 24
    global in2 = 23
    global en = 25

    global in4 = 20
    global in5 = 16
    global en3 = 21

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(en,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(in5,GPIO.OUT)
    GPIO.setup(en3,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

    global speed = GPIO.PWM(en,1000)
    global speed3 = GPIO.PWM(en3,1000)
    #default speed
    speed.start(25)

def callback0(data):
    #runs everytime button changes
    arr = data.drive
    if arr[0] == 2:
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
    if arr[1] == 2:
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(in5,GPIO.LOW)
    if arr[0] == 1:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
    if arr[1] == 1:
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.HIGH)
    else:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.LOW)

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
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.LOW)