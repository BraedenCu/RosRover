import pygame

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

def run():
    while True:
        pygame.event.pump()
        print(pygame.joystick.Joystick(0).get_axis(0))

        if pygame.joystick.Joystick(0).get_button(0):
            print("a pushed")
        
        if pygame.joystick.Joystick(0).get_button(1):
            print("b pushed")
        
        if pygame.joystick.Joystick(0).get_button(2):
            print("x pushed")
        
        if pygame.joystick.Joystick(0).get_button(3):
            print("y pushed")

if __name__ == '__main__':
    setup()
    run()
    
