# most generic way to define functions
def print_super_wargs(*args, **kwargs):
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print "{} -> {}".format(key, value)


# kwargs are keyword arguments
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print "{} -> {}".format(key, value)


# takes any number of arguments
def print_args(*args):
    for arg in args:
        print(arg)

print_args("red", "blue", "green")
print_kwargs(r="red", b="blue", g="green")




