#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from lxml import etree
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")
key = config.get("Settings", "API_KEY")

if key == 'sample_key':
	raise Exception("Something went wrong, probably you forgot to paste your yandex.speechkit key into settings.ini")
	
def rec(data):
	''' принимает на вход аудио файл, распознает речь, если не удалось возвращает код ошибки'''
	if key == 'sample_key':
		raise Exception("Something went wrong, probably you forgot to paste your yandex.speechkit key into settings.ini")
	url = 'https://asr.yandex.net/asr_xml?uuid=01ae13cb544628b48fb536d496daa1e6&key='+key+'&topic=queries'
	headers = {"Content-Type": 'audio/x-wav'}
	response = requests.post(url, headers=headers, data=data)
	if response.status_code==200:
		return parseXML(response.content)
	else:
		raise Exception("Cant recognize speech"+str(response.status_code))

def parseXML(xmlFile):
	'''
	Принимает на вход файл из функции rec(), парсит его, 
	возвращает первое значение из массива файлов, которые были получены при распознавании
	'''
	root = etree.fromstring(xmlFile)	
	l=[]
	for variant in root.getchildren():
		if not variant.text:
			text = "None"
		else:
			l.append(variant.text)
	if len(l) == 0:
		print('Ничего не найдено')
		return('')
	else:
		return(l[0])
