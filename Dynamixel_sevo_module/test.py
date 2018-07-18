import servocontrol
import threading
import sys
import time
import queue
import Chbh 
import Timer 
sys.path.insert(0, '../Alisnky')
from DataBase import *
sys.path.insert(2, '../recognition')
from parsing_bml import *
q = queue.Queue()

def m1():
    Chbh.master(q)

def s1():
    Timer.slaver(q)

mastert = threading.Thread(target=m1)
mastert.start()
slavert = threading.Thread(target=s1)
slavert.start()
