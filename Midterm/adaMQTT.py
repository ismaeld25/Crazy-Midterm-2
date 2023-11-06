import mqtt
import sys
import time
import Y5
import HdW
#Y5.connect() #connects to wifi

ada_url='io.adafruit.com'
username='IsmaelD25'
key='aio_aslj69LJqyQkcr00odxhJkZrPZmD'
mqtt_client_id= bytes('client_'+'12321','utf-8')
id_temp='thermal-reads'

client=mqtt.MQTTClient(client_id=mqtt_client_id,server=ada_url,user=username,password=key,ssl=False)
try:
    client.connect()
    print('connected?')
except exception as e:
    print('could not connect to MOTT server {}}'.format (type(e).__name__,e))
    sys.exit()
temp_feed = bytes('{:s}/feeds/{:s}'.format(username, id_temp), 'utf-8') # format - techiesms/feeds/temp

HdW.Tmeter(28)
client.publish(temp_feed,bytes(str(HdW.Tmeter(28)),'utf-8'),qos=0)