import random

def try_except():
    try:
        a = 1/random.random()
        # Random generates number in range 0,1 so ZeroDivisionError possible
    except ZeroDivisionError:
        a = 0
    # Cath more than one type of error
    except SystemError:
        a = None
    return a

print(try_except())
print("Done")

###

# Raise an error
# Exceptions occur, because somebody raised them
b = random.random()
if b == 0:
    raise ZeroDivisionError
else:
    b = 1/b
print(b)