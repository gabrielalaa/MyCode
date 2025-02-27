for c in "Happy birthday":
    print(c)

i = iter("Happy birthday")
print(i)
# <str_iterator object at 0x0000022050384070>

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# H
# A
# P
# P
# Y

# You don't want to control it

###################################


# For this to be an iterable object, it has to return an iter
class MyRange:
    def __init__(self, start=0, end=0, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current = self.start - self.step

    # I have the iter
    def __iter__(self):
        return self

    # I can call the next value
    def __next__(self):
        # self.start += self.step
        self.current += self.step
        if self.current >= self.end:
            raise StopIteration
        return self.current


for c in MyRange(0, 10, 3):
    print(c)