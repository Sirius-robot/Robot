import pyaudio
import wave
from array import array

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
		print('zapis')
        frames.append(data)
    else:
        print("nothing")

stream.stop_stream()
stream.close()
audio.terminate()
wavfile=wave.open(FILE_NAME,'wb')
wavfile.setnchannels(CHANNELS)
wavfile.setsampwidth(audio.get_sample_size(FORMAT))
wavfile.setframerate(RATE)
wavfile.writeframes(b''.join(frames))#append frames recorded to file
wavfile.close()