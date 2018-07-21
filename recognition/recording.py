#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyaudio
import wave
from array import array
import msvcrt
import configparser

def writetofile(frames, countfile):
	
	wavfile=wave.open('recording'+str(countfile)+'.wav','wb')
	wavfile.setnchannels(CHANNELS)
	wavfile.setsampwidth(audio.get_sample_size(FORMAT))
	wavfile.setframerate(RATE)
	wavfile.writeframes(b''.join(frames))#append frames recorded to file
	wavfile.close() 
	
FORMAT=pyaudio.paInt16
CHANNELS=2
RATE=44100
CHUNK=1024

config = configparser.ConfigParser()
config.read("../settings.ini")
VOLUME = int(config.get("Settings", "VOLUME"))
COUNTSTART = int(config.get("Settings", "COUNTSTART"))
COUNTEND = int(config.get("Settings", "COUNTEND"))


audio=pyaudio.PyAudio() 
stream=audio.open(format=FORMAT,channels=CHANNELS, 
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK)

#начало записи 
frames=[]
#пока уровень шума меньше 390 запись не ведется, если больше, то начинается запись в файл
n_end=0
n_start=0
record=False
countfile = 0
cache_frames = []
while True:
	data=stream.read(CHUNK)
	data_chunk=array('h',data)
	vol=max(data_chunk)
	if record is True:
		frames.append(data)
		if (vol>=VOLUME):
			n_end = 0
		else:
			n_end += 1
			if n_end > COUNTEND:
				countfile += 1
				writetofile(frames, countfile)
				print("recording stop")
				record = False
				with open('recording'+str(countfile)+'.wav','rb') as file:
					data = file.read()
				#print(chatbot.chat_bot(rec(data)))
				n_start = 0
	else: 
		if (vol >= VOLUME):
			cache_frames.append(data)
			n_start += 1
			if n_start > COUNTSTART:				
				frames = cache_frames
				record = True
				print('voice recording')
				n_end = 0				
		else:
			n_start = 0
			cache_frames = []
			

stream.stop_stream()
stream.close()
audio.terminate()



