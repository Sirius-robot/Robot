from lxml import etree
import requests
import recognition
import configparser
import threading
import queue
from array import array
import wave
import sys
import time
import pyaudio

sys.path.insert(0, 'recognition')
from recognition import rec
import chatbot

FORMAT=pyaudio.paInt16
CHANNELS=1
RATE=16000
CHUNK=1024
RECORD_SECONDS=15

def writetofile(frames, sampwidth, countfile):
	wavfile=wave.open('recording'+str(countfile)+'.wav','wb')
	wavfile.setnchannels(CHANNELS)
	wavfile.setsampwidth(sampwidth)
	wavfile.setframerate(RATE)
	wavfile.writeframes(b''.join(frames))
	wavfile.close() 

def process(q, frames, sampwidth, countfile):	
	writetofile(frames, sampwidth, countfile)
	with open('recording'+str(countfile)+'.wav','rb') as file:
		data = file.read()
		print(sys.getsizeof(data))
	if sys.getsizeof(data) < pow(2,19):
		print("put in queue")
		q.put(chatbot.chat_bot(rec(data)))
	else:
		q.put(chatbot.chat_bot('абрикосики4847'))

def recording(q, event,eventio):
	config = configparser.ConfigParser()
	config.read("settings.ini")
	VOLUME = int(config.get("Settings", "VOLUME"))
	COUNTSTART = int(config.get("Settings", "COUNTSTART"))
	COUNTEND = int(config.get("Settings", "COUNTEND"))
	audio=pyaudio.PyAudio() 
	stream=audio.open(format=FORMAT,channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
	n_end=0
	n_start=0
	record=False
	countfile = 0
	cache_frames = []
	t = None
	cache_audio = []
	while not event.is_set():
		data=stream.read(CHUNK)
		data_chunk=array('h',data)
		vol=max(data_chunk)
		#print(sys.getsizeof(data))
		if t != None:
			if not t.is_alive():
				if len(cache_audio)> 0:
					t = threading.Thread(target=process, args=(q, cache_audio.pop(0), audio.get_sample_size(FORMAT), countfile))
					t.start()
		if record is True:
			frames.append(data)
			if (vol>=VOLUME):
				n_end = 0
			else:
				n_end += 1
				if n_end > COUNTEND:
					countfile += 1
					print("recording stop")
					record = False
					n_start = 0
					n_end = 0
					if t == None:
						t = threading.Thread(target=process, args=(q, frames, audio.get_sample_size(FORMAT), countfile))
						t.start()
					else:
						cache_audio.append(frames)
						if not t.is_alive():
							t = threading.Thread(target=process, args=(q, cache_audio.pop(0), audio.get_sample_size(FORMAT), countfile))
							t.start()
					frames = []
		else: 
			if (vol >= VOLUME):
				cache_frames.append(data)
				n_start += 1
				if n_start > COUNTSTART:
					frames = cache_frames
					cache_frames = []
					record = True
					print('voice recording')
					n_end = 0
					n_start = 0

	if t != None:
		t.join()
	stream.stop_stream()
	stream.close()
	audio.terminate()

