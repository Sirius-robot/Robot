#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyaudio
import wave
from array import array
from lxml import etree
import requests

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
	
def zapisvfail():
	wavfile=wave.open(FILE_NAME,'wb')
	wavfile.setnchannels(CHANNELS)
	wavfile.setsampwidth(audio.get_sample_size(FORMAT))
	wavfile.setframerate(RATE)
	wavfile.writeframes(b''.join(frames))#append frames recorded to file
	wavfile.close() 

def rec():
	url = 'https://asr.yandex.net/asr_xml?uuid=01ae13cb544628b48fb536d496daa1e6&key=697bb904-b1f7-4c36-acec-104bc87a04ff&topic=queries'
	headers = {"Content-Type": 'audio/x-wav'}
	with open('RECORDING.wav', 'rb') as file:
		data = file.read()
		response = requests.post(url, headers=headers, data=data)
		if response.status_code==200:
			with open('text.xml','wb') as file:
				file.write(response.content)	
FORMAT=pyaudio.paInt16
CHANNELS=2
RATE=44100
CHUNK=1024
RECORD_SECONDS=15
FILE_NAME="RECORDING.wav"


audio=pyaudio.PyAudio() 
stream=audio.open(format=FORMAT,channels=CHANNELS, 
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK)

#начало записи 
frames=[]
#пока уровень шума меньше 500 запись не ведется, если больше, то начинается запись в файл
for i in range(0,int(RATE/CHUNK*RECORD_SECONDS)):
    data=stream.read(CHUNK)
    data_chunk=array('h',data)
    vol=max(data_chunk)
    if(vol>=500):
        frames.append(data)

stream.stop_stream()
stream.close()
audio.terminate()
zapisvfail()


rec()

if __name__ == "__main__":
    s=parseXML("text.xml")
print(s)

