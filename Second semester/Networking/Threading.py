import threading


def printIntNumbers(code):
    for i in range(100):
        print(code, 1)


# Create a thread
t1 = threading.Thread(target=printIntNumbers, args=('Apple',))
t2 = threading.Thread(target=printIntNumbers, args=('Banana',))

# printIntNumbers('Apple')
# printIntNumbers('Banana')

# Both are running in parallel
t1.start()
t2.start()