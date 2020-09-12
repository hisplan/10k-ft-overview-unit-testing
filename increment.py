from random import randint


def inc1(x):
    """Increment by 1"""
    return x + 1


def inc2(x, n):
    """Increment by n"""
    return x + n


def inc3(x):
    """Increment by a random number"""
    return x + randint(1, 100)


if __name__ == "__main__":

    x = 4

    print(inc1(x))
    print(inc2(x, 2))
    print(inc3(x))
