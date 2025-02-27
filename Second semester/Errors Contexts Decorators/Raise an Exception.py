class NumberIsNotOddException(Exception):
    pass


def abc():
    i = int(input("Enter a number: "))
    if i % 2 == 0:
        raise NumberIsNotOddException


try:
    abc()
except:
    print("Number was even")