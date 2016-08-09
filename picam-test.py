from picamera import PiCamera
from time import sleep
camera = PiCamera()

camera.hflip=True
camera.vflip=True

for i in range(5):
	sleep(1)
	#camera.capture('/home/pi/picam-test/image%s.jpg' % i)
	camera.capture('image{0:04d}.jpg'.format(i))
	

	
#camera.start_recording('video.h264')
#sleep (5)
#camera.stop_recording()

print("done")
