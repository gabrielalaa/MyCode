# Define 3 decorators

def underline(f):
    def f3():
        return f"<u>{f()}</u>"
    return f3

def italic(f):
    def f2():
        return f"<i>{f()}</i>"
    return f2

def bold(f):
    def f1():
        return f"<b>{f()}</b>"
    return f1

# Apply the decorators
@bold
@italic
@underline
def mp():
    return "hello world"

# Test the function
print(mp())