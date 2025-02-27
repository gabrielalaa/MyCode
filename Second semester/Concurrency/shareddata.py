import threading

x = 0
lock = threading.Lock()

def increment ():
    global x
    global lock
    for i in range (1000):
        lock.acquire()
        x = x+1
        lock.release()

def decrement ():
    global x
    global lock
    for i in range (10000):
        lock.acquire()
        x = x-1
        lock.release()


t1 = threading.Thread(target=increment)
t1.start()
print ("t1 started")
t2 = threading.Thread(target=decrement)
t2.start()
print ("t2 started")

t1.join ()
t2.join()

print ("X is", x)
