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

#camera warm up
camera.start_preview()
sleep(2)

#camera capture
print('capture start')
for i in range(20):
	camera.capture('image{0:04d}.jpg'.format(i))
	sleep(.25)
camera.close()
endTime = time.time()
print('capture end, time elapsed=',endTime - startTime, 's')


#convert jpgs to gif
print('convert to gif start')
system('convert -delay 25 -loop 0 image*.jpg animation.gif')

endTime = time.time()
print('done, total time=', endTime-startTime, 's')
