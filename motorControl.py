#!/usr/bin/env python3.6
import rospy
import rospy
from std_msgs.msg import String,Int32,Int32MultiArray,MultiArrayLayout,MultiArrayDimension, Int16MultiArray
#rosroverxbox is the name of the package, and IntList is the name of the .msg file
import RPi.GPIO as GPIO          
from time import sleep

def init():

    GPIO.setwarnings(False)

    global in1 
    global in2
    global en
    global in5
    global in6
    global en3
    global speed
    global speed3
    global in3
    global in4
    global en2
    global in7
    global in8
    global en4
    global speed2
    global speed4

    #.
    in1 = 23
    in2 = 24
    en = 18
    #.
    in3 = 20
    in4 = 16
    en2 = 21
    #.
    in5 = 13
    in6 = 19
    en3 = 26
    #.
    in7 = 4
    in8 = 17
    en4 = 27

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(en,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(en2,GPIO.OUT)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in5,GPIO.OUT)
    GPIO.setup(in6,GPIO.OUT)
    GPIO.setup(en3,GPIO.OUT)
    GPIO.output(in5,GPIO.LOW)
    GPIO.output(in6,GPIO.LOW)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in7,GPIO.OUT)
    GPIO.setup(in8,GPIO.OUT)
    GPIO.setup(en4,GPIO.OUT)
    GPIO.output(in7,GPIO.LOW)
    GPIO.output(in8,GPIO.LOW)

    speed = GPIO.PWM(en,1000)
    speed2 = GPIO.PWM(en2,1000)
    speed3 = GPIO.PWM(en3,1000)
    speed4 = GPIO.PWM(en4,1000)

    #default speed
    speed.start(75)
    speed2.start(75)
    speed3.start(75)
    speed4.start(75)

def callback0(data):
    #runs everytime button changes
    arr = data.data
    print(".")

    #set speed to 75 percent
    speed.ChangeDutyCycle(75)
    speed2.ChangeDutyCycle(75)
    speed3.ChangeDutyCycle(75)
    speed4.ChangeDutyCycle(75)

    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in5,GPIO.LOW)
    GPIO.output(in6,GPIO.LOW)
    GPIO.output(in7,GPIO.LOW)
    GPIO.output(in8,GPIO.LOW)

    #3,4 and 5,6 are a pair
    #1,2 and 7,8 are a pair

    if arr[0] == 1:

        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in8,GPIO.LOW)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in7,GPIO.HIGH)


    if arr[0] == -1:

        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in8,GPIO.HIGH)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in7,GPIO.LOW)

    if arr[1] == 1:
        
        GPIO.output(in5,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in6,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)

    if arr[1] == -1:
        
        GPIO.output(in5,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in6,GPIO.HIGH)
        GPIO.output(in4,GPIO.HIGH)
        
    if arr[0] == 0 or arr[1] == 0:  
        #stop  
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.LOW)
        GPIO.output(in6,GPIO.LOW)
        GPIO.output(in7,GPIO.LOW)
        GPIO.output(in8,GPIO.LOW)

def listener():

    rospy.init_node('motorControl', anonymous=True)

    rospy.Subscriber('driver', Int32MultiArray, callback0)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        init()
        listener()
    except rospy.ROSInterruptException:
        GPIO.cleanup()
  