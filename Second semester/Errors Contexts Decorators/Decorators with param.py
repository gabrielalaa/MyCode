def calledBy(callerName):
    def decorator(f):
        def funcCall (*args,**kwargs):
            return callerName + " says " + f(*args, **kwargs)
        return funcCall
    return decorator

@calledBy('Markus')
def sayHello(name):
    return f'Hello {name}'

print(sayHello('Robert'))
# Markus says Hello Robert

####################################################

def font(*args, **kwargs):
    def inner(x):
        return f'<font size="{kwargs["size"]}" color="{kwargs["color"]}">{x}</font>'
    def inner2(original_function):
        return lambda : inner(original_function())
    return inner2

@font(size=12, color="red")
def mp():
    return "hello world"
print(mp())

# "<font size="12" color="red>hello world</font>