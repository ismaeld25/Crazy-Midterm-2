##Essentially
import time
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


##servo
from machine import Pin, PWM
def Servo():
    marg= 200_000 #may need adjustment
    servopw= PWM(Pin(12))
    servopw.freq(50)
    ang=500_000 #zero
    car=''
    while True:#car.lower() !='q': #q to stop
        ang=(100_000*int(input())) #type non integer to crash out of loop lol
        servoDuty= ang
        servopw.duty_ns(servoDuty)
        print(ang)
    #50000 is lowest, 2500000 is max
import HdW
HdW.Tmeter(28)

#7-19 to go from 32 to 86 Fah