#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from lxml import etree
def rec():
	url = 'https://asr.yandex.net/asr_xml?uuid=01ae13cb544628b48fb536d496daa1e6&key=697bb904-b1f7-4c36-acec-104bc87a04ff&topic=queries'
	headers = {"Content-Type": 'audio/x-wav'}
	with open('RECORDING.wav', 'rb') as file:
		data = file.read()
		response = requests.post(url, headers=headers, data=data)
		if response.status_code==200:
			with open('text.xml','wb') as file:
				file.write(response.content)

def parseXML(xmlFile):
	with open(xmlFile, encoding = 'utf-8') as f_obj:
		xml = f_obj.read().encode('utf-8')
	root = etree.fromstring(xml)	
	l=[]
	for variant in root.getchildren():
		if not variant.text:
			text = "None"
		else:
			l.append(variant.text)
		return(l[0])
 
 
rec()
if __name__ == "__main__":
    s=parseXML("text.xml")
print(s)