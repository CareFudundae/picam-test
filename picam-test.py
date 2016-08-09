from picamera import PiCamera
from time import sleep
from os import system
camera = PiCamera()

camera.hflip=True
camera.vflip=True

for i in range(5):
	#sleep(1)
	#camera.capture('/home/pi/picam-test/image%s.jpg' % i)
	camera.capture('image{0:04d}.jpg'.format(i))
	
system('convert -delay 10 -loop 0 image*.jpg animation.gif')
	
#camera.start_recording('video.h264')
#sleep (5)
#camera.stop_recording()

print('done')
