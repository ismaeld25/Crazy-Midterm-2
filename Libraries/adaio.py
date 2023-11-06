import urequests as requests
import ujson

print(reply.status_code) #test

def ADA(unit):
    #test
    y='heee'
    
    USERNAME = 'IsmaelD25'
    #print('Here is what the Adafruit code does')
    url = 'https://io.adafruit.com/api/v2/%s/feeds' % USERNAME
    key = 'aio_aslj69LJqyQkcr00odxhJkZrPZmD'
    headers = {'X-AIO-Key':key,'Content-Type':'application/json'}
    reply = requests.get(url,headers=headers)

    #print(reply.status_code)
    #if reply.status_code == 200:
    reply = reply.json() #a JSON array of info
    keys = [x['key'] for x in reply]
    groups = [x['group']['name'] for x in reply]
    names = [x['name'] for x in reply]
    values = [x['last_value'] for x in reply]
    GROUP = 'midterm'
    if unit == 'green':
        FEED_KEY = 'thermal-reads'
    if unit == 'red':
        FEED_KEY = 'thermal-reads-celsius'
    url = 'https://io.adafruit.com/api/v2/%s/feeds/%s.%s/data' % (USERNAME, GROUP, FEED_KEY)
    return url, reply, keys, groups, names, values, GROUP, FEED_KEY, y

def VALUE(val):
    #test
    print(y)
    
    data = {'value':val}
    print(url)
    print(reply)
    replyposts = requests.post(url,headers=headers,json=data) #posting
    print('reply now is', replyposts.status_code)
    replygets = requests.get(url,headers=headers) #getting
    print(val)