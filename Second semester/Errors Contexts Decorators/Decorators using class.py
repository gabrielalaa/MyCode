class Execute_3_times:
    def __init__(self, function):
        self.function = function
    def __call__(self):
        self.function()
        self.function()
        self.function()

@Execute_3_times
def function():
    print("Hello")
# function = Execute_3_times(function)

function()
# function.__call__()