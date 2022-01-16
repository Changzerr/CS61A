""" Lab 04 Optional Questions """

from lab04 import *

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []

    知识点：
    >>> round(10.5)
    10
    >>> round(10.51)
    11
    """
    "*** YOUR CODE HERE ***"
    return [round(sqrt(s[i])) for i in range(len(s)) if sqrt(s[i]) == round(sqrt(s[i]))]

def key_of_min_value(d):
    """Returns the key in a dict d that corresponds to the minimum value of d.
    >>> letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}
    >>> min(letters)
    'a'
    >>> key_of_min_value(letters)
    'c'

    知识点：
    >>> min([-1, 0, 1])                    # no key argument; return smallest input
    -1
    >>> min([-1, 0, 1], key=lambda x: x*x) # return input with the smallest square
    0
    """
    "*** YOUR CODE HERE ***"
    return min(d,key=lambda x: d[x])
