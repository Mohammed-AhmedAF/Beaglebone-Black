import Adafruit_BBIO.GPIO as GPIO
from time import sleep

topButton = "P9_11"
bottomButton = "P9_13"
GPIO.setup(topButton,GPIO.IN)
GPIO.setup(bottomButton,GPIO.IN)

while(1):
    if GPIO.input(topButton):
        print("Top button is pushed")
    if GPIO.input(bottomButton):
        print("Bottom button is pushed")
    if GPIO.input(bottomButton) and GPIO.input(topButton):
        print("Break")
        break
    #Used to debounce the switches
    sleep(.2)

print("Good bye, come back again!")
GPIO.cleanup()

