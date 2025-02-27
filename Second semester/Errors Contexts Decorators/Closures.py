# This is the outer enclosing function
def print_msg(msg):
    # This is the nested function
    def printer():
        print(msg)
    # returns the nested function
    return printer

# Now let's try calling this function.
another = print_msg("Hello")
another()