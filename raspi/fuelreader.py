#!/usr/bin/env python3

import base64
import json
import requests
import time
from picamera import PiCamera
from time import sleep



def main():

	# Take picture
	print("Taking picture")
	current_time_millis = millis = int(round(time.time() * 1000))	
	image_file_name = str(current_time_millis) + ".jpg"
	image_file_path = "/home/pi/fuel-reader/data/fresh/" + image_file_name

	camera = PiCamera()
	camera.start_preview()
	camera.capture(image_file_path)
	camera.stop_preview()	

	# Base64 encode picture
	print("Base64 encoding")
	image_file = open(image_file_path, 'rb')
	image_content = image_file.read()
	base64_content = base64.encodestring(image_content).decode("utf-8")

	print("Posting to AWS")
	url = "https://nmsdi43zjf.execute-api.us-east-1.amazonaws.com/uat/readings"
	request_object = dict()
	request_object["ImageName"] = image_file_name
	request_object["Image64"] = base64_content
	request_json = json.dumps(request_object)	
	response = requests.post(url, data = request_json)
	print(response.text)
	

if __name__ == "__main__":
	main()


