from lxml import etree
import requests
import recognition
from recognition import rec
import chatbot
import configparser
import threading
import queue
import pyaudio
from array import array
import wave
import sys
import time
import msvcrt

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
        print("No error")
    else:
        q.put(chatbot.chat_bot('абрикосики4847'))

def recording(q, event, eventio):
    config = configparser.ConfigParser()
    config.read("settings.ini")
    VOLUME = int(config.get("Settings", "VOLUME"))
    COUNTSTART = int(config.get("Settings", "COUNTSTART"))
    COUNTEND = int(config.get("Settings", "COUNTEND"))
    
    audio=pyaudio.PyAudio() 
    stream=audio.open(format=FORMAT,channels=CHANNELS, 
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK)
    n_end=0
    n_start=0
    record=False
    countfile = 0
    t = None
    cache_audio = []  
    frames = []  
    while not event.is_set():
        if t != None:
            if not t.is_alive():
                if len(cache_audio)> 0:
                    t = threading.Thread(target=process, args=(q, cache_audio.pop(0), audio.get_sample_size(FORMAT), countfile))
                    t.start()
        if record is True:
            data=stream.read(CHUNK)
            frames.append(data)
            key = None
            lock = threading.Lock()
            with lock:
                if msvcrt.kbhit():
                    key = msvcrt.getch()
            if key == b" ":
                print("stop recording")
                countfile += 1
                record = False                
                if t == None:
                    t = threading.Thread(target=process, args=(q, frames, audio.get_sample_size(FORMAT), countfile))
                    t.start()
                else:
                    cache_audio.append(frames)
                    if not t.is_alive():
                        t = threading.Thread(target=process, args=(q, cache_audio.pop(0), audio.get_sample_size(FORMAT), countfile))
                        t.start()
        else:
            key = None
            lock = threading.Lock()
            with lock:
                if msvcrt.kbhit():
                    key = msvcrt.getch()           
            if key == b" ":
                record = True
                frames = []
                print("voice recording")

    if t != None:
        t.join()
    stream.stop_stream()
    stream.close()
    audio.terminate()

    
    