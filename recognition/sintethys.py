import requests
import winsound

def speech(text):
	URL = 'https://tts.voicetech.yandex.net/generate?text='+text+'&format=wav&lang=ru-RU&speaker=ermil&key=697bb904-b1f7-4c36-acec-104bc87a04ff&speed=1&emotion=good'
	response=requests.get(URL)
	if response.status_code==200:
		return response.content
	else:
		raise Exception("Cant synthesize speech"+response.status_code)


