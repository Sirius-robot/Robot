#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyaudio
import wave
from array import array
from lxml import etree
import requests
import msvcrt
from msvcrt import getch

FORMAT=pyaudio.paInt16
CHANNELS=2
RATE=44100
CHUNK=1024
RECORD_SECONDS=15

def writetofile(frames, countfile):
	
	wavfile=wave.open('recording'+str(countfile)+'.wav','wb')
	wavfile.setnchannels(CHANNELS)
	wavfile.setsampwidth(audio.get_sample_size(FORMAT))
	wavfile.setframerate(RATE)
	wavfile.writeframes(b''.join(frames))#append frames recorded to file
	wavfile.close() 

key=msvcrt.getch()

if key==b'\r': #нужно нажать enter
	audio=pyaudio.PyAudio() 
	stream=audio.open(format=FORMAT,channels=CHANNELS, 
					  rate=RATE,
					  input=True,
					  frames_per_buffer=CHUNK)

	#начало записи 
	frames=[]
	#пока уровень шума меньше 500 запись не ведется, если больше, то начинается запись в файл
	n=0
	record=False
	countfile = 0
	while True:
		if record is True:
			print('record')
			data=stream.read(CHUNK)
			data_chunk=array('h',data)
			vol=max(data_chunk)
			frames.append(data)
			if (vol>=390):
				n=0
			else:
				n=n+1
				if n>7:
					countfile += 1
					writetofile(frames, countfile)
					record = False
		else: 
			data=stream.read(CHUNK)
			data_chunk=array('h',data)
			vol=max(data_chunk)
			if(vol>=500):
				frames=[]
				record = True
				frames.append(data)
				n=0
	if key==b'\r':		
		stream.stop_stream()
		stream.close()
		audio.terminate()