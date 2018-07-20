import requests
import configparser

import winsound
config = configparser.ConfigParser()
config.read("../settings.ini")
key = config.get("Settings", "API_KEY")

def speech(text):
	'''
	функция принимает на вход значение text в котором содержится текст который будет синтезироваться, возвращает записанный звук 
	'''
	if key == 'sample_key':
		raise Exception("Something went wrong, probably you forgot to paste your yandex.speechkit key into settings.ini")
	URL = 'https://tts.voicetech.yandex.net/generate?text='+text+'&format=wav&lang=ru-RU&speaker=ermil&key='+key+'&speed=1&emotion=good'
	response=requests.get(URL)
	if response.status_code==200:
		return response.content
	else:
		raise Exception("Cant synthesize speech "+str(response.status_code))





