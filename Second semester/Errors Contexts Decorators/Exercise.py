class log:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, func):
        def wrapped_func(*args, **kwargs):
            with open(self.filename, 'a') as f:  # Open in append mode
                f.write(f"{args[0]}\n")  # Write the first argument (str1) to the file
            return func(*args, **kwargs)
        return wrapped_func

@log("test.txt")
def m1(str1):
    print(str1)

# Call the function multiple times
m1("hello1")
m1("suny")
m1("hell2o")
m1("hel2lo")