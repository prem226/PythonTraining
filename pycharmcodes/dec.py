from functools import wraps
def decor2(func):
    def inner():
        x = func()
        print("x in decor3", x)
        return x + x

    return inner

def decor1(func):
    def inner():
        x = func()
        print("x in decor2", x)
        return x * x

    return inner


def decor(func):
    def inner():
        x = func()
        print("x in decor 1st..", x)
        return 2 * x

    return inner

@decor2
@decor1
@decor
def num():
    return 10

num()