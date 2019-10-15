"""
Fib module.
"""
import timeit
import numpy as np
import matplotlib.pyplot as plt

def fibb(n):
    fib1=fib2=1
    i = 2
    while i < n:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        i += 1
    return fib_sum;

def fib(n: int) -> int:
    """Fib implementation.

    :param n: Argument of function.
    :type n: int
    :returns: Result of function.
    :rtype: int

    Examples.
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(6)
    8
    """
    assert n >= 0
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def speedup(f):
    tab = {}

    def f1(x):
        if x not in tab:
            tab[x] = f(x)
        return tab[x]

    return f1


def bench(f):
    return timeit.timeit(f, number=100)

def fact(x):
    if x > 0:
        return fact(x-1) * x
    else:
        return 1

def rec(b):
    if b == 0:
        return 1
    else:
        return 9 * rec(b-1)

fast_fib = speedup(fibb)
fast_fact = speedup(fact)
fast_rec = speedup(rec)

x = 40



values = [
    bench(lambda: rec(300)),
    bench(lambda: fast_rec(300)),

]

plt.bar(['fib', 'fast_fib'], values)
plt.show()

