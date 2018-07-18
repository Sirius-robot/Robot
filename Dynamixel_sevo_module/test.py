import servocontrol
import threading
import sys
import time
import queue
from chbh import *
from timer import *
sys.path.insert(0, '../Alisnky')
from DataBase import *
sys.path.insert(1, '../Sinthesis')
from sinthesis import *
sys.path.insert(2, '../recognition')
from parsing_bml import *

def m1():
    master()

def s1():
    slaver()

mastert = threading.Thread(target=m1)
mastert.start()
slavert = threading.Thread(target=s1)
slavert.start()
