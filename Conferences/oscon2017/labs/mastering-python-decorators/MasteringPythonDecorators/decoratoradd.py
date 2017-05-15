def add(increment):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return increment + func(*args, **kwargs)
        return wrapper
    return decorator


@add(3)
def f(n):
    return n + 2

print f(4)

# ---------------------------------


def multiply(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return num * func(*args, **kwargs)
        return wrapper
    return decorator


@multiply(2)
def m(n):
    return n

print m(9)

