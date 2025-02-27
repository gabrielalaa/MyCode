# Finally clauses will always happen, even if there's a return beforehand
def example():
    try:
        return "Returning from try block"
    finally:
        print("Finally block executed")

print(example())

# Finally block executed
# Returning from try block

###

# Exceptions in the finally clause are nested within the prior saved exception
def example():
    try:
        1 / 0  # This raises a ZeroDivisionError
    finally:
        raise ValueError("An error in finally")  # This raises a ValueError

try:
    example()
except Exception as e:
    print(f"Caught: {e}")

# Caught: An error in finally

###

#  Break and return statements within finally will delete the saved exception
def example():
    try:
        raise KeyError("An exception")
    finally:
        return "Returning from finally"

print(example())

# Returning from finally

###

# If the try is in a loop, continue will execute the finally clause before restarting the loop, and break will execute the finally before leaving
for i in range(3):
    try:
        if i == 1:
            continue
    finally:
        print(f"Finally for i = {i}")

# Finally for i = 0
# Finally for i = 1
# Finally for i = 2

for i in range(3):
    try:
        if i == 1:
            break
    finally:
        print(f"Finally for i = {i}")

# Finally for i = 0
# Finally for i = 1