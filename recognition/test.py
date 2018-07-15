import multiprocessing
import time
# bar
def bar():
    for i in range(100):
        print ("Тик-так")
        time.sleep(1)

if __name__ == '__main__':
    # Запустить bar как процесс
    p = multiprocessing.Process(target=bar)
    p.start()

    # Ждать 10 секунд или пока процесс завершится сам
    p.join(10)

    # Если всё ещё жив - прибить
    if p.is_alive():
        print ("Жив!.. ПРИБИТЬ!!")
        p.terminate()
        p.join()