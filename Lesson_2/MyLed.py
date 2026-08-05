from machine import Pin
from time import sleep 
sleep(0.5)
MyLed=Pin(15,Pin.OUT)

MyLed.value(1)