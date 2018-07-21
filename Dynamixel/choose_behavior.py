import servocontrol
import threading
import sys
import time
import queue

sys.path.insert(0, 'Alisnky')
from DataBase import *
#sys.path.insert(1, '../Sinthesis')
#from sinthesis import *
sys.path.insert(2, 'recognition')
from parsing_bml import *


def choose_behavior(chbh_to_timer):
    db = database()
    big_dict = {}
    while 1:
        f = open('bml/vvv.bml', 'r')
        z = f.read()
        x = dictionary_result(z)
        gestur = x['figure'] 	
        texts = x['speech']
        mouth = x['mouth']
        brows = x['brows']
        pupils = x['pupils']
        if len(gestur) > 0:
            if len(gestur[0]) > 0:
                command_data = db.gesture(gestur[0])
                eye_data = db.eyes(gestur[0])
                time_dict = {}
                for commands_time in command_data:
                    timew = commands_time[0]
                    commands = commands_time[1]
                    ids = []
                    angles = []
                    dif_times = []
                    for command in commands:
                        ids.append(command[0])
                        angles.append(command[1])
                        dif_times.append(command[2])
                        time_dict[timew] = [ids, angles, dif_times]  
                big_dict['command_motor'] = time_dict
            if len(eye_data):
                time_pointz=[]
                cordx=[]
                cordy=[]
                delta_time=[]
                for i in eye_data:
                    time_pointz.append(i[0])
                    cordx.append(i[1])
                    cordy.append(i[2])
                    delta_time.append(i[3])
                print('TIME')
                print(time_pointz)
                print(cordx)
                print(cordy)
                print(delta_time)
                comeyez={'time_points':time_pointz,'cordx':cordx,'cordy':cordy,'delta_time':delta_time}
                big_dict['command_eye'] = comeyez
        if len(texts) > 0:
            big_dict['speech'] = texts
        if len(mouth) > 0:
            big_dict['img_mouth'] = mouth
        if len(brows) > 0:
            big_dict['img_brows'] = brows
        if len(pupils) > 0:
            big_dict['pupils'] = pupils
        chbh_to_timer.put(big_dict)
        if len(texts) > 0:
            if len(texts[0])>0:
                print(texts[0])
                #audio = speech(texts[0])
                #winsound.PlaySound(audio, winsound.SND_MEMORY)
        # sinthesis.speech(text)
        #if text =
        time.sleep(5)