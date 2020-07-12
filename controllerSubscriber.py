#!/usr/bin/env python3.6
import rospy
import rospy
from std_msgs.msg import String,Int32,Int32MultiArray,MultiArrayLayout,MultiArrayDimension, Int16MultiArray
#rosroverxbox is the name of the package, and IntList is the name of the .msg file
from cleaningbot.msg import IntList
import RPi.GPIO as GPIO          
from time import sleep

def init():

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

def forward(x1,y1):
    GPIO.output(x1,GPIO.LOW)
    GPIO.output(y1,GPIO.HIGH)

def turnRight(x1,x2,y1,y2):
    GPIO.output(x1,GPIO.LOW)
    GPIO.output(x2,GPIO.HIGH)
    GPIO.output(y1,GPIO.HIGH)
    GPIO.output(y2,GPIO.LOW)

def turnLeft(x1,x2,y1,y2):
    GPIO.output(x1,GPIO.HIGH)
    GPIO.output(x2,GPIO.LOW)
    GPIO.output(y1,GPIO.LOW)
    GPIO.output(y2,GPIO.HIGH)

def backward(x1,x2):
    GPIO.output(x1,GPIO.HIGH)
    GPIO.output(x2,GPIO.LOW)

def stop(x1,x2):
    GPIO.output(x1,GPIO.LOW)
    GPIO.output(x2,GPIO.LOW)

def callback0(data):
    #runs everytime button changes
    arr = data.drive
    print(".")

    #set speed to 75 percent
    speed.ChangeDutyCycle(75)
    speed2.ChangeDutyCycle(75)
    speed3.ChangeDutyCycle(75)
    speed4.ChangeDutyCycle(75)
    
    if arr[0] == 1:
        #move forward
        forward(in2,in1)
        forward(in4,in3)
        forward(in6,in5)
        forward(in8,in7)

    elif arr[0] == 2:
        #move backwards
        forward(in1,in2)
        forward(in3,in4)
        backward(in5,in6)
        backward(in7,in8)

    elif arr[1] == 1:
        #turn right
        turnRight(in1,in2,in5,in6)
        turnRight(in3,in4,in7,in8)

    elif arr[1] == 2:
        #turn left
        turnRight(in5,in6,in1,in2)
        turnRight(in7,in8,in4,in5)

    elif arr[0] == 0 or arr[1] == 0:  
        #stop  
        stop(in1,in2)
        stop(in3,in4)
        stop(in5,in6)
        stop(in7,in8)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('driver', IntList, callback0)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        init()
        listener()
    except rospy.ROSInterruptException:w
        GPIO.cleanup()
