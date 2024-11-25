# *args -> It is used when we dont know number of arguments user going to give. Or 
# It is a way to allow a function to accept a variable number of positional arguments.

# it collects all the positional arguments passed to the function and packs them into a tuple.

def sum_all(*args):
    print(args) # prints tuple of all the inputs
    s = 0
    for i in args:
        s += s + i
    return s
    # return sum(args) # we can do this instead of above

print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 6, 4, 9))
# print(sum_all(1))
# print(sum_all(1, 2, 3, 8))
