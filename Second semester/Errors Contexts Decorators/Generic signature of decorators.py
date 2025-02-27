def my_decorator(f):
    def f1(*args, **kwargs):
        print ("before ")
        f(*args, **kwargs)
        print ("after ")
    return f1

@my_decorator
def fy(t):
    print(t)

@my_decorator
def fx(t, name="silly"):
    print(t, name)

fx(10)
fy(20)

############################

def my_decorator(f):
    def f1(xyz):
        print("before hello")
        f(xyz)  # Call the original function with the parameter
        print("after hello")
    return f1

@my_decorator
def hello(xyz):
    print(f"hello {xyz}")

# Now define `xyz` before calling the function
xyz = "world"
hello(xyz)