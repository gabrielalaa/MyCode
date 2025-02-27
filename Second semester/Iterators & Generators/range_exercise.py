# a.
def myrange(start, stop, step):
    for i in range(start, stop):
        if start <= stop:
            yield start
        start += step

for c in myrange(0,10,3):
    print (c)

###

# b.
def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step

for c in frange(0.3,10.2,3.2):
    print (c)