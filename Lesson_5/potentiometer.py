import machine
from time import sleep

pot28=28

potA=machine.ADC(pot28)


while True:
    potAvalue=potA.read_u16()
    voltage=(3.3/65106)*potAvalue-(430*3.3/65106)
    print(voltage)
    sleep(0.3)