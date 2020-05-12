
import pygame
import rospy
from std_msgs.msg import String,Int32,Int32MultiArray,MultiArrayLayout,MultiArrayDimension

def setup():

    pygame.display.init()
    pygame.joystick.init()
    pygame.joystick.Joystick(0).init()
    # Prints the joystick's name
    JoyName = pygame.joystick.Joystick(0).get_name()
    print("Name of the joystick:")
    print(JoyName)
    # Gets the number of axes
    JoyAx = pygame.joystick.Joystick(0).get_numaxes()
    print("Number of axis:")
    print(JoyAx)

def publishData():
    pub = rospy.Publisher('inputs', Int32MultiArray, queue_size=10)
    rospy.init_node('controller', anonymous=True)
    rate = rospy.Rate(10)
    data_arr = [0, 0, 0, 0, 0, 0, 0]
    dataarr = []

    while not rospy.is_shutdown():

        pygame.event.pump()

        rightX = pygame.joystick.Joystick(0).get_axis(0)
        rightY = pygame.joystick.Joystick(0).get_axis(1)
        leftX = pygame.joystick.Joystick(0).get_axis(2)
        leftY = pygame.joystick.Joystick(0).get_axis(3)

        data_arr.insert(0, rightX)
        data_arr.insert(1, rightY)
        data_arr.insert(2, leftX)
        data_arr.insert(3, leftY)

        if pygame.joystick.Joystick(0).get_button(0):
            data_arr.insert(4, 1)
        
        if pygame.joystick.Joystick(0).get_button(1):
            data_arr.insert(5, 1)
        
        if pygame.joystick.Joystick(0).get_button(2):
            data_arr.insert(6, 1)
        
        if pygame.joystick.Joystick(0).get_button(3):
            data_arr.insert(7, 1)
        
        else:
            data_arr.insert(4, 0)
            data_arr.insert(5, 0)
            data_arr.insert(6, 0)
            data_arr.insert(7, 0)
        
        #publish data array
        dataarr = Int32MultiArray(data=data_arr)
        #dataarr.data = [x for x in data_arr]
        rospy.loginfo(dataarr)
        pub.publish(dataarr)

        rate.sleep()

if __name__ == '__main__':
    setup()
    publishData()
    