import time

def remember(fn):
    timeToRemember = None
    print("this is magic")

    def inner(*args, **kwargs):
        nonlocal timeToRemember
        if timeToRemember is None:
            timeToRemember = fn(*args, **kwargs)
        return timeToRemember
    return inner

@remember
def m1():
    return time.time()

@remember
def m2(name):
    print(name)
    return time.time()

# Test the functionality
print(m1())
time.sleep(2)
print(m1())  # Should return the same result as the first call

m2("same")

###########################################################################

import time

def remember(f):
    local_time = None
    def change_time(*args, **kwargs):
        nonlocal local_time
        if local_time is None:
            local_time = f(*args, **kwargs)
        return local_time

    return change_time

@remember
def m1():
    return time.time()

print(m1())
print(m1())