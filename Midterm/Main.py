#Code is a work in progress, currently missing for loops

import machine
from machine import Pin, UART
import uasyncio as asyncio
import time
import HdW

starttime=time.time()

#no Airtable so here are colors
#color=input('')
waita=.1
async def sense():
    HdW.Tmeter(28)
    await asyncio.sleep(waita)
    #val.append(bank)
    return val

async def servo(x):
    print('Putting Val in',sense.val)
    x=sense.val
    HdW.Servo(val)
    await asyncio.sleep(waita)
    
async def main(duration):
    asyncio.create_task(sense())
    asyncio.create_task(servo(x))
    await asyncio.sleep(duration)

def test(duration):
    try:
        asyncio.run(main(duration)) #start everything running
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        asyncio.new_event_loop()  #end loop
        print('clear state')
test(5)
