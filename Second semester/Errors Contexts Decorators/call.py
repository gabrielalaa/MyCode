class ABC:
    def __call__(self):
        print("Hello")


ab1 = ABC()
ab1()
# without __call__:
# TypeError: 'ABC' object is not callable