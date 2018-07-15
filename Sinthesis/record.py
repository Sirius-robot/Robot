import requests

def speech(text):
	URL = 'https://tts.voicetech.yandex.net/generate?text='+text+'&format=mp3&lang=en-EN&speaker=ermil&key=697bb904-b1f7-4c36-acec-104bc87a04ff&speed=1&emotion=good'
	response=requests.get(URL)
	if response.status_code==200:
		with open('1.mp3','wb') as file:
			file.write(response.content)
		return response.content
speech('Hello')