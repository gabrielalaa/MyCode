def SquaresSum():
    s = 0
    for i in range(1, 101):
        s += i**2
    return s


def SumSquare():
    s = 0
    for i in range(1, 101):
        s += i
    return s**2


def SumSquareDifference():
    return SumSquare() - SquaresSum()


print(SumSquareDifference())