# # f = None
#
#
# def silly():
#     a = input()
#     print(1 / int(a))
#     # global f
#     # f = open("input.txt", "r")
#
#
# try:
#     silly()
# except ZeroDivisionError:
#     print("ZeroDivisionError occurred")
# except ValueError as err:
#     print("ValueError occurred", err)
# # Optional
# else:
#     print("No error occurred")
# # It will be executed always:
# finally:
#     print("Goodbye")
#
# # Finally can be used for example to close a file in the end


f = None
def silly():
    a = input ()
    global f
    f = open ("daf.txt", "w")


    print (1/int(a))


try:
    silly()
except ZeroDivisionError:
    print ("Zero division Error occured")
except ValueError as error:
    print ("Value error occured ", error)
else:
    print ("No error occured")
finally :
    print ("the end of code ")
    f.close()