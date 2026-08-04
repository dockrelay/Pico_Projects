from machine import Pin
from time import sleep

##creating an object myled
##LED IS HOW THE ONBoard pico led is referenced

                  # IF i WAS READING DATA FROM IT WOULD BE AN INPUT 
myled=Pin('LED',Pin.OUT) # I AM SEDING DATA TO IT THEREFORE OUTPUT ,"Pin.OUT"

while True:

    myled.value(0)
    sleep(0.3)
    myled.value(1)
    sleep(0.3)
