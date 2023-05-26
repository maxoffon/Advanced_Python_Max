from threading import Semaphore, Thread
import time

sem: Semaphore = Semaphore()


def fun1():
    while True:
        sem.acquire()
        print(1)
        sem.release()
        time.sleep(0.25)


def fun2():
    while True:
        sem.acquire()
        print(2)
        sem.release()
        time.sleep(0.25)


t1: Thread = Thread(target=fun1)
t2: Thread = Thread(target=fun2)
t1.daemon = True
t2.daemon = True
t1.start()
t2.start()
try:
    while t1.is_alive():
        pass
except KeyboardInterrupt:
    print('\nReceived keyboard interrupt, quitting threads.')