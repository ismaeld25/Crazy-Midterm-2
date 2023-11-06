import cv2 as cv
cv2_image = cv2.cvtColor(np.array(cam.raw_image), cv2.COLOR_RGB2BGR)
b,g,r = cv2.split(cv2_image)
grey = cv2.cvtColor(cv2_image, cv2.COLOR_BGRA2GRAY)
cam.show(grey)  # shows any cv2 image in the same spot on the webpage (third image)
image3 = Image.fromarray(grey)
display(Image.fromarray(r),Image.fromarray(g),Image.fromarray(b))
key='patNbmPRVD5NwBjfM.ed9074299f1c316ec699d00ec2b5c68627aa6551d3f87e854ef948999a5979d7'
#cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([cv2_image],[i],None,[256],[0,256])
    plt.plot(histr,color = col)  # add the different histograms to the plot
    plt.xlim([0,256])  # define x axis length (cuts off some of the picture)

plt.imshow(r)  # puts red image in the background
display(plt)  #shows it
ret,thresh1 = cv2.threshold(r,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(b,127,255,cv2.THRESH_BINARY)
ret,thresh3 = cv2.threshold(g,127,255,cv2.THRESH_BINARY)

rav=np.sum(thresh1) #gets sum of colors
print("here",rav)
bav=np.sum(thresh2)
print("here",bav)
gav=np.sum(thresh3)
print("here",gav)
if gav > rav and bav:
    print("this image is green")
if rav > gav and bav:
    print('this image is red')
if bav > gav and rav:
    print('this image is blue')

if reply.status_code == 200:
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
