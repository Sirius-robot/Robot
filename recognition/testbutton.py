
#!/usr/bin/python
# -*- coding: utf-8 -*-
import msvcrt
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

def writetofile(frames):
	
	wavfile=wave.open('recording''''+str(countfile)'''+'.wav','wb')
	wavfile.setnchannels(CHANNELS)
	wavfile.setsampwidth(audio.get_sample_size(FORMAT))
	wavfile.setframerate(RATE)
	wavfile.writeframes(b''.join(frames))#append frames recorded to file
	wavfile.close() 

	
	
def button():
	done = False
	record=False
	while not done:
		if msvcrt.kbhit():
			print ("you pressed",msvcrt.getch(),"so now i will quit")
			if record is True:
				frames.append(data)
				stream.stop_stream()
				print('record oveer')
				record =False
				stream.close()
				audio.terminate()
				done =  True
			else:
				audio=pyaudio.PyAudio() 
				stream=audio.open(format=FORMAT,channels=CHANNELS, 
								rate=RATE,
								input=True,
								frames_per_buffer=CHUNK)
				
				frames=[]
				record =True
				print('record')
				data=stream.read(CHUNK)
				frames.append(data)
				#writetofile(frames)
		
		else:
			if record is True:
				frames.append(data)
		

					
button()

		
		
					
					
					
					


			




