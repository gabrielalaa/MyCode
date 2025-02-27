# Each function has a __closure__ attribute
def print_in_a_box(x):
    # The nested function must refer to a value defined in the enclosing function
    boxchar = "+"   # Local variable
    # The enclosing function must return the nested function
    def myprint():  # This is an inner function that will print the string x inside a "box" made up of the character boxchar
        print (boxchar*len(x)*2)
        print ("| "+x + " |")
        print(boxchar * len(x)*2)
    return myprint  # it returns a function that can be called later.

# Create a closure
f = print_in_a_box("Happy")  # x = "Happy" and boxchar = "+" are remembered inside the myprint function, even after print_in_a_box has finished executing
# The __closure__ attribute of a function holds the data it has remembered from its surrounding environment. Each remembered variable is stored in a cell, and you can access it using cell_contents
# __closure__[0] would store the value of boxchar = "+"
print (f.__closure__[1].cell_contents)

# Closures can avoid the use of global values and provides some form of data hiding
# Encapsulation: The inner function retains access to the environment it was created in, which can provide some level of data hiding