from queue import Queue
import queue, pygame, win32api, win32gui, win32con, time
import thread_putinqu, thread_event_handling
from threading import Thread, Event
from pygame.locals import *
from feature import Feature
from face import Face

waitEvent = Event()
waitEvent.set()         #waitEvent.isSet() return True

que = Queue()       #   queue for images. На вход подается список из двух строк.
                    #    1 строка - имя файла для новых бровей
                    #    2 строка - имя файла для новой улыбки
                    #    если 1 строка пустая, то изображение для бровей не меняется. аналогично с улыбкой
                    #    иф пустой список, то лицо приходит в нормальное состояние,
                    #     Рразмер зрачка

que_pup = Queue()   #    список из конечных координат и времени за которое надо прийти в точку.

pygame_thread_mypygame= Thread(target=thread_event_handling.main_pygame, args = (que, que_pup, waitEvent))
pygame_thread_mypygame.start()

pygame_thread_putinqu = Thread(target=thread_putinqu.putinqu, args = (que, que_pup, waitEvent))
pygame_thread_putinqu.start()
try:
    pygame_thread_putinqu.join()
    pygame_thread_mypygame.join()

except KeyboardInterrupt:
    waitEvent.clear()