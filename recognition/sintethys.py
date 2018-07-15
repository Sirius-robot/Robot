import requests
import configparser

config = configparser.ConfigParser()
config.read("../settings.ini")
key = config.get("Settings", "API_KEY")


def speech(text):
        if key == 'sample_key':
                raise Exception("Something went wrong, probably you forgot to paste your yandex.speechkit key into settings.ini")
	URL = 'https://tts.voicetech.yandex.net/generate?text='+text+'&format=wav&lang=ru-RU&speaker=ermil&key='+key+'&speed=1&emotion=good'
	response=requests.get(URL)
	if response.status_code==200:
		return response.content
	else:
		raise Exception("Cant synthesize speech"+response.status_code)






