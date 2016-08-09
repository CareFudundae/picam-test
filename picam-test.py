from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.hflip=True
camera.vflip=True

for i in range(3):
	sleep(3)
	camera.capture('/home/pi/picam-test/image%s.jpg' % i)
