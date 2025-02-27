import time
import threading
import random

def countFunction (name):
    count = 0
    while count <= 10:
        print(name + str(count))
        count += 1
        time.sleep(random.random())
    return

t1 = threading.Thread(target=countFunction, args=("A",))
t1.start()