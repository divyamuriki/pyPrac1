import importlib


def string_up_low(in_str):
    upper = ""
    lower = ""
    num = ""
    for letter in in_str:
        if letter.isupper():
            upper += letter
        elif letter.islower():
            lower += letter
        else:
            num += letter

    print(upper)
    print(lower)
    print(num)


# factorial
def fact(n):
    fac = 1
    for i in range(1, n + 1):
        fac = fac * i
    print(fac)


# fibinacii
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(7))
