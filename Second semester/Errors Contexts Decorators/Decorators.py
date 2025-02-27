def my_decorator1(original_method):
    def f1(*args, **kwargs):
        print ("before ", original_method.__name__)
        original_method(*args, **kwargs)
        print ("after", original_method.__name__)
    return f1

def my_decorator2(original_method):
    def f1(*args, **kwargs):
        print ("before ", original_method.__name__)
        original_method(*args, **kwargs)
        print ("after", original_method.__name__)
    return f1

@my_decorator2 # before f1
@my_decorator1 # before fy
def fy(t):
    print(t) # ha
fy("ha")
# after fy
# after f1

@my_decorator1
@my_decorator2
def fy(t):
    print(t)
fy("ha")

##########################################################3

# change the behavior of another func
# = a func which manages another func
# = an obj that takes a func and returns another func
# also called metaprogramming

def my_decorator(f):
    def f1():
        print ("before hello")
        f()
        print ("after hello")
    return f1

# this becomes f1
@my_decorator
# <=> hello = my_decorator(hello)
def hello():
    print("hello")

hello()