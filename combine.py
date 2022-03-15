import threading
import time


def mon11():
    import mon1

def mon21():
    import mon2

def mon31():
    import mon3





x = threading.Thread(target=mon11, args=())
x.start()

w = threading.Thread(target=mon21, args=())
w.start()

y = threading.Thread(target=mon31, args=())
y.start()






w.join()
x.join()
y.join()






print(time.perf_counter())
