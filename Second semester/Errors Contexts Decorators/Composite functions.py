# Functions are objects, so we can pass them as arguments to other functions

# Functions that can accept other functions as arguments are also called higher-order functions

def run_this(f):
    print ("before exec")
    f()
    print ("after exec")

def hi():
    print("hello")

run_this(hi)