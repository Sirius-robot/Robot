#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

''':
	URL = 'https://asr.yandex.net/asr_xml?uuid=01ae13cb544628b48fb536d496daa1e6&key=697bb904-b1f7-4c36-acec-104bc87a04ff&topic=queries'
	#param = {'uuid': '01ae13cb544638b48fb536d496daa1e6', 'key': '697bb904-b1f7-4c36-acec-104bc87a04ff', 'topic': 'queries'}

	with open('RECORDING.wav','rb') as file:
		files = {'upload_file': file}
		headers = {'Content-Type': 'audio/x-wav'} #audio/x-mpeg-3
		response = requests.post(URL, headers=headers, files=files)
		print(response.status_code,response.content)
		if response.status_code==200:
			print(response.content)
			with open('text.xml','wb') as file:
				file.write(response.content)
	return 
speech()'''
def rec():
	url = 'https://asr.yandex.net/asr_xml?uuid=01ae13cb544628b48fb536d496daa1e6&key=697bb904-b1f7-4c36-acec-104bc87a04ff&topic=queries'
	headers = {"Content-Type": 'audio/x-wav'}
	with open('RECORDING.wav', 'rb') as file:
		data = file.read()
		response = requests.post(url, headers=headers, data=data)
		print(response.status_code)
		if response.status_code==200:
			print(response.content)
			with open('text.xml','wb') as file:
				file.write(response.content)
rec()
#data = open('RECORDING.wav', 'rb').read()
 
'''response = requests.post(url, headers=headers, data=data)
print(response.status_code)
if response.status_code==200:
	print(response.content)
	with open('text.xml','wb') as file:
		file.write(response.content)'''