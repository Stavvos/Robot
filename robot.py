#import curses and GPIO
import curses
import RPi.GPIO as GPIO

class Robot:
#get the curses window, turn off echoing of keyboard to screen,
#turn on instant key responses, use special values for cursor keys
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)
#set the GPIO pins
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup (7,GPIO.OUT)
    GPIO.setup (11,GPIO.OUT)
    GPIO.setup (13,GPIO.OUT)
    GPIO.setup (15,GPIO.OUT)

#define functions U = Up, D = Down , L = Left, R = Right and S = Stop.
    def L (self):
        GPIO.output(7,True)
        GPIO.output(11,False)
        GPIO.output(13,True)
        GPIO.output(15,False)
        print("Left")

    def R (self):
        GPIO.output(7,False)
        GPIO.output(11,True)
        GPIO.output(13,False)
        GPIO.output(15,True)
        print("Right")

    def D (self):
        GPIO.output(7,True)
        GPIO.output(11,False)
        GPIO.output(13,False)
        GPIO.output(15,True)
        print ("Down")

    def U (self):
        GPIO.output(7,False)
        GPIO.output(11,True)
        GPIO.output(13,True)
        GPIO.output(15,False)
        print ("Up")

    def S (self):
        GPIO.output(7,False)
        GPIO.output(11,False)
        GPIO.output(13,False)
        GPIO.output(15,False)
        print ("Stop")

#decalre object
object = Robot()
#Open a loop with the exit condition being the "q" key.
#Call function if key press condition is met.
#10 = enter key on the keyboard
try:
    while True:
        screen = object.screen
        char = screen.getch()
        if char == ord ('q'):
            break
        elif char == curses.KEY_UP:
            object.U()
        elif char == curses.KEY_DOWN:
            object.D()
        elif char == curses.KEY_LEFT:
            object.L()
        elif char == curses.KEY_RIGHT:
            object.R()
        elif char == 10:
            object.S()
finally:
    #close down loop properly
    curses.nocbreak(); screen.keypad (0); curses.echo(); curses.endwin()
    GPIO.cleanup() 