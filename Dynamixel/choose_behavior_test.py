
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

def choose_behavior(chbh_to_timer,eventio,bh_end,q,eventi):
    db = database()
    big_dict = {}
    while 1:
        if not q.empty():
            bmlname = q.get()
            path = ""
            for d in os.listdir("Bml/"):
                if os.path.isfile(os.path.join('Bml', d, bmlname+'.bml')):
                    path = os.path.join('Bml', d, bmlname+'.bml')
            if path != "":
                with open(path, 'r') as f:
                    z = f.read()
                x = dictionary_result(z)
                gestur = x['figure']
                mouth = x['mouth']
                brows = x['brows']
                pupils = x['pupils']
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
                if len(mouth) > 0:
                    big_dict['img_mouth'] = mouth
                if len(brows) > 0:
                    big_dict['img_brows'] = brows
                if len(pupils) > 0:
                    big_dict['pupils'] = pupils
                chbh_to_timer.put(big_dict)
                print(bh_end.get())
                eventio.wait()
            else:
                print("No bml file found")
                eventio.set()