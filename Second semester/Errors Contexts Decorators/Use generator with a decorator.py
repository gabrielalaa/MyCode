import contextlib

# It changes the behavior of the function
@contextlib.contextmanager
def mycontext (p):
    print ("Create Context") # enter part
    yield "c-Object"
    print ("Clear Context") # exit part

with mycontext("") as c:
    print (c)

print ("after the context", c)