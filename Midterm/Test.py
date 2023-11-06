import adaio

adaio.ADA('red')
adaio.VALUE(51)


#try y=heeee in first def and returning it as a print statement on the second def

#hardware code
import machine
from machine import Pin, UART
import uasyncio as asyncio
import time

fred = Pin(5, Pin.OUT, Pin.PULL_UP) #LED
shag = Pin(6, Pin.OUT, Pin.PULL_UP)

def LED(color):
    if color ==1:
        shag.off()
        fred.on()
        print('C')
    elif color ==2:
        fred.off()
        shag.on()
        print('F')
    else:
        fred.off()
        shag.off()

marg= 200_000 #may need adjustment
servopw= PWM(12)
servopw.freq(50)
ang=2_000_000 #may need adjustment
servoDuty= ang
servopw.duty_ns(servoDuty)

def gauge():
    global servoDuty
    if servoDuty - marg < ang:
        servopw.duty_ns(servoDuty)
    else:
        servoDuty= servoDuty - marg #may need adjustment so the ratio of duty to degrees is correct
        servopw.duty_ns(servoDuty)
        print(servoDuty)


#UART Code
waita= 1

async def tempread():
    temp=pin.value() #this should be the value the pico reads from the thermoster
    await asyncio.sleep(waita)
    
    
async def servo():
    