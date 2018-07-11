import requests
import winsound

def speech(text):
	URL = 'https://tts.voicetech.yandex.net/generate?text='+text+'&format=wav&lang=ru-RU&speaker=ermil&key=697bb904-b1f7-4c36-acec-104bc87a04ff&speed=1&emotion=good'
	response=requests.get(URL)
	#try:
	if response.status_code==200:
		return response.content
	else:
		raise Exception("")
	#except response.status_code!=200:
	#	print('bad sound or smth wrong with language, audio format, etc')
	#else: 
	#	return response.content

text = "Проголосуйте в телеграме"
audio = speech(text)
with open(text+'.wav','wb') as file:
	file.write(audio)
winsound.PlaySound(text+'.wav', winsound.SND_FILENAME)
