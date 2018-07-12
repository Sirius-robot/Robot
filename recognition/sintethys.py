import requests
#import winsound
import configparser
config = configparser.ConfigParser()
config.read("../settings.ini")
key = config.get("Settings", "API_KEY")
def speech(text):
	URL = 'https://tts.voicetech.yandex.net/generate?text='+text+'&format=wav&lang=ru-RU&speaker=ermil&key='+key+'&speed=1&emotion=good'
        #print(URL)
	response=requests.get(URL)
	if response.status_code==200:
		return response.content
	else:
		raise Exception("Cant synthesize speech"+response.status_code)


bina = speech('Privet Mir')
file = open("testfile.wav","w") 
file.write(bina) 
file.close() 


