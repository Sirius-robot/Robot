import servocontrol
import threading
import sys
import time
import queue
import os
import sys
import time
import random

sys.path.insert(0, 'Alisnky')
from DataBase import *
sys.path.insert(1, 'Sinthesis')
from sinthesis import *
sys.path.insert(2, 'recognition')
from parsing_bml import *
from th_recognitionwithbutton import *

def choose_behavior(chbh_to_timer,event_end,bh_end,q,eventi):
    db = database()
    global txt
    global tag
    event_end.set()
    while 1:
        global tagxt
        if not q.empty():
            tagxt = q.get()
            print(tagxt)
            tag = tagxt[1]
            txt = tagxt[0]
            chbh_to_timer.put(prep_gest(db,tag,txt))
        elif chbh_to_timer.empty() and event_end.is_set():
            tag = 'inactivity'
            chbh_to_timer.put(prep_gest(db,tag))



def prep_gest(db,tag,txt=''):
    big_dict = {}
    print(tag)
    print(txt)
    with open(os.path.join('Bml',tag, random.choice(os.listdir("Bml/"+tag))), 'r') as f:
        z = f.read()
        y = z.replace("<speech>", "<speech>" + txt)
    x = dictionary_result(y)
    gestur = x['figure']
    texts = x['speech']
    mouth = x['mouth']
    brows = x['brows']
    pupils = x['pupils']

    print(texts )
    file_name = None
    if texts != ['']:
        file_name = (texts[0][:20]+'.wav')
        invalid_sym = ["?","\'","\"",":","*","\\","/","<",">","|"]
        for sym in invalid_sym:
            file_name = file_name.replace(sym, "")
        if os.path.isfile(file_name) == False:
            textz = speech(texts[0])
            with open(file_name, 'wb') as file:
                file.write(textz)
    if len(gestur) > 0:
        if len(gestur[0]) > 0:
            command_data = db.gesture(gestur[0])
            eye_data = db.eyes(gestur[0])
            if (len(eye_data) == 0 and len(command_data) == 0):
                print("gesture doesn't exist")
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
            pupils_time_pointz_dictionary = {}
        for i in eye_data:
            if i[-1] == 0:
                pupils_time_pointz_dictionary[-2] = i[1:4]
            else:
                pupils_time_pointz_dictionary[i[0]] = i[1:4]

    if len(pupils_time_pointz_dictionary) > 0:
        big_dict['command_eye'] = pupils_time_pointz_dictionary
    if file_name != None:
        big_dict['speech'] = file_name
        print('file'+file_name)
    if len(mouth) > 0:
        big_dict['img_mouth'] = mouth
    if len(brows) > 0:
        big_dict['img_brows'] = brows
    if len(pupils) > 0:
        big_dict['pupils'] = pupils
    return big_dict