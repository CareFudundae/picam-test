from picamera import PiCamera
from time import sleep
import time
from os import system

startTime = time.time()
camera = PiCamera()

camera.hflip=True
camera.vflip=True
#camera.resolution=(1024,768)
camera.resolution=(320,240)

for i in range(4):
	camera.capture('image{0:04d}.jpg'.format(i))
	sleep(.5)
	
endTime = time.time()
print(endTime - startTime, ' seconds')
	
system('convert -delay 25 -loop 0 image*.jpg animation.gif')
	
#camera.start_recording('video.h264')
#sleep (5)
#camera.stop_recording()

endTime = time.time()
print(endTime - startTime, ' seconds')
print('done')
