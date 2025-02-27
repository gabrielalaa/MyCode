# class mycontext():
#     def __init__(self, p):
#         self.p = p
#
#     def __enter__(self):
#         # When you enter, you create it first
#         print("Create Context")
#         return "c-object"  # This is the context object
#
#     def __exit__(self, exception, value, trace):
#         print("Clear Context")
#
#
# with mycontext("Something") as c:
#     print("in the context")
#     print(c)
#
# print("after the context", c)
#
# ##############################################
#
# # Example:
# class my_file_opener:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def __enter__(self):
#         self.file = open(self.filename)
#         return self.file
#
#     def __exit__(self, exception, value, trace):
#         self.file.close()
#
#
# with my_file_opener("Thread Class.py") as myself:
#     print(myself.read())

class mycontext():
    def __init__ (self, p):
        self.p = p
    def __enter__(self):
        print ("Create Context")
        return "c-object"
    def __exit__(self, exception, value, trace):
        print ("Clear Context")


with mycontext("Hypp") as contextobj:

    print ("in the conext")
    print (contextobj)

print("after", contextobj)

# Example
class myfileopener ():

    def __enter__(self):
        self.file = open (__file__)
        return self.file

    def __exit__(self, exception, value, trace):
        self.file.close()

with myfileopener() as myself:
    print (myself.read() )