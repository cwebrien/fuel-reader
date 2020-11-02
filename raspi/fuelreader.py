#!/usr/bin/env python3


from picamera import PiCamera
from time import sleep



def main():
	camera = PiCamera()
	camera.start_preview()
	for i in range(5):
		sleep(5)
		print("Captured image%s", i)
		camera.capture('image%s.jpg' % i)
	camera.stop_preview()




if __name__ == "__main__":
	main()


