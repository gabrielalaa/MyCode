# Something about errors will be in the final exam
def xx():
    a = 10

    try:
        print(a / 0)
    except:
        print("error occurred")
    else:
        print("all good")
    finally:
        print("Now at the end")


def yy():
    a = 10
    print(a / 0)


# You can have different locations for those errors - exception handling
# I can have more functions which check the main ones: xx, yy.
def aa():
    yy()


def bb():
    try:
        aa()
    except:
        print("error occurred")


xx()

# You can also manage the error here:
# You can have different locations for those errors - exception handling
# I can have more functions which check the main ones: xx, yy.
try:
    # yy()
    bb()
except:
    print("error in yy")