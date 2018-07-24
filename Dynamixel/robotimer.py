
import threading
import sys
import time
import queue
import wave
import contextlib
from collections import defaultdict
sys.path.insert(3, 'Dynamixel_sevo_module')
from servocontrol import *
import choose_behavior
sys.path.insert(0, 'Alisnky')
from DataBase import *
sys.path.insert(1, 'Sinthesis')
from sinthesis import *
sys.path.insert(2, 'recognition')
from parsing_bml import *

global max_time_val

max_time_val = 0
time_iter = -40

def roberttimer(chbh_to_timer,timer_to_images,timer_to_eyepos,eventio,bh_end):
    global anglea
    multiInt((1, 2, 3, 4, 5, 6))

    anglea = multiread([1, 2, 3, 4, 5, 6])

    def work_time(time_iter):
        return time_iter + 40

    def timer1():
        global time_iter
        global max_time_val
        global time_dict_motors
        global command_eye
        threading.Timer(0.04, timer1).start()
        if time_dict_motors == None and command_eye == None:
            if not chbh_to_timer.empty():
                eventio.clear()
                big_dict = chbh_to_timer.get()
                if 'img_mouth' in big_dict:
                    mouth = big_dict['img_mouth']
                else:
                    mouth = ''

                if 'img_brows' in big_dict:
                    brows = big_dict['img_brows']
                else:
                    brows = ''

                if 'pupils' in big_dict:
                    pupils = big_dict['pupils']
                else:
                    pupils = 100

                timer_to_images.put([brows[0], mouth[0], int(pupils[0])])
                if 'command_eye' in big_dict:
                    command_eye = big_dict['command_eye']
                   
                if 'speech' in big_dict:
                    speech = big_dict['speech']
                    with contextlib.closing(wave.open(speech,'r')) as f:
                        frames = f.getnframes()
                        rate = f.getframerate()
                        duration = frames / float(rate)
                        print(duration)
                        dur = duration * 1000
                        if dur > max_time_val:
                            max_time_val = dur
                        print(speech)
                        winsound.PlaySound(speech, winsound.SND_FILENAME|winsound.SND_ASYNC)


                if 'command_motor' in big_dict:
                    time_dict_motors = big_dict['command_motor']
                    print(time_dict_motors)
                    datauy = time_dict_motors[-2]
                    for z in range(len(datauy[0])):
                        datauy[2][z] = datauy[1][z]/1024*300
                    robotControl(datauy[0], datauy[2], datauy[1], anglea)
                    for i in range(len(datauy[0])):
                        anglea[datauy[0][i]] = datauy[1][i]

        else:
            time_iter = work_time(time_iter)
            if time_iter > max_time_val:
                max_time_val = 0
                time_iter = -40

                time_dict_motors, command_eye = None, None
                bh_end.put("The END!")
                timer_to_images.put([])
                eventio.set()
            if  not command_eye == None:
                if command_eye.get(time_iter, -666) != -666:
                    timer_to_eyepos.put(command_eye[time_iter])
                    if command_eye[time_iter][-1] + time_iter > max_time_val:
                        max_time_val = command_eye[time_iter][-1] + time_iter
            if time_dict_motors != None:
                if time_dict_motors.get(time_iter, -666) != -666:
                    datauy = time_dict_motors[time_iter]
                    for y in datauy[2]:
                        if y + time_iter > max_time_val:
                            max_time_val = y + time_iter
                    time1 = time.time()
                    robotControl(datauy[0], datauy[2], datauy[1], anglea)
                    time2 = time.time()
                    print(time2-time1)
                    for i in range(len(datauy[0])):
                        anglea[datauy[0][i]] = datauy[1][i]
    global time_dict_motors
    global command_eye 
    time_dict_motors, command_eye = None, None                    
    timer1()



