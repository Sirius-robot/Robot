from queue import Queue
import queue, pygame, win32api, win32gui, win32con, time
import sys
sys.path.insert(0,"face/programm")
import thread_putinqu, thread_event_handling
from threading import Thread, Event
from pygame.locals import *

waitEvent = Event()
waitEvent.set()     #waitEvent.isSet() return True

que = Queue()       #   queue for images. На вход подается список из двух строк.
                    #    1 строка - имя файла для новых бровей
                    #    2 строка - имя файла для новой улыбки
                    #    если 1 строка пустая, то изображение для бровей не меняется. аналогично с улыбкой
                    #    иф пустой список, то лицо приходит в нормальное состояние,
                    #     Рразмер зрачка

que_pup = Queue()   #    список из конечных координат и времени за которое надо прийти в точку.


try:
    pygame_thread_mypygame = Thread(target=thread_event_handling.main_pygame, args=(que, que_pup, waitEvent))
    pygame_thread_mypygame.daemon = True
    pygame_thread_mypygame.start()

    pygame_thread_putinqu = Thread(target=thread_putinqu.putinqu, args=(que, que_pup, waitEvent))
    pygame_thread_putinqu.daemon = True
    pygame_thread_putinqu.start()
    while True:
        time.sleep(100)


except (KeyboardInterrupt, SystemExit):
    print('ok')
    waitEvent.clear()
    pygame_thread_putinqu.join()
    pygame_thread_mypygame.join()