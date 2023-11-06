#This code is used for all the hardware
import time
import machine
import utime
import math
from machine import Pin, PWM

def timer():
    starttime=time.time()
    while True:
        current_time=time.time()
        deltTime=current_time - starttime
        print(deltTime)
        if deltTime > 5:
            start_send=1
            print('5 minutes!')
            starttime=time.time()
        else:
            start_send=0
            #run main(duration)
        time.sleep(1)

def Tmeter(tPin):
    global Fah
    global val
    global Cel
    therm=machine.ADC(tPin) #28
    er=60 #calibration
    therm_val =therm.read_u16()
    Vr=3.3*float(therm_val)/65535
    Rt=1000000*Vr/(3.3-Vr)
    temp=1/(((math.log(Rt/1000000))/3950)+(1/(273.15+25)))
    Cel=temp-273.15-er
    Fah=Cel*1.8 +32
    utime.sleep_ms(200)
    val = 15000*Fah
    print(Fah,val)
    return Fah, Cel, val
    #numbers found from SunFounder.com but adjusted to work for me

def Servo(val):
    bottom= 1_900_000
    top=700_000
    marg= 200_000 #may need adjustment
    servopw= PWM(Pin(12)) #12
    servopw.freq(50)
    ang=(bottom*(1-(val/89)))-32 #range of movement
    print(ang)
    servoDuty=ang
    servopw.duty_ns(int(servoDuty))
    return ang
# while True: #troubleshooting
#     Tmeter(28)
#     print(Fah)
#     time.sleep(1)
