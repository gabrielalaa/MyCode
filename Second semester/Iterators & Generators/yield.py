def x():
    return 5


def y():
    # It will return a next
    yield 5
    yield 6
    yield 111
    yield 123456789


print(x())

# You get an iterator
i = y()
# The function waits for the next call
print(next(i))
print(next(i))
print(next(i))
print(next(i))


# OR
for a in y():
    print(a)

################################################

def mygen():
    yield("C")
    yield("G")
    yield("A")
    yield("T")

gen = mygen()
print (next(gen))  # C
print (next(gen))  # G

for c in gen:
    print (c)
# A
# T

gen = mygen()
print (list (gen))  # ['C', 'G', 'A', 'T']