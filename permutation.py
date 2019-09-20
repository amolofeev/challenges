"""
https://en.wikipedia.org/wiki/Permutation

Recursion + generators.
In spite of recursive algorithm we'll never get MaxRecursionLimit exception because of our stack size always == N.
Therefore, if we want to get MaxRecursionLimit we have to call permutation function with array of 333+ items.
"""


def factorial(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


def permutation(in_, parents=None):
    parents = parents or ()
    for i in range(len(in_)):
        new_in = in_[:]
        v = new_in[i]
        del new_in[i]
        if new_in:
            yield from permutation(new_in, parents + (v,))
        else:
            yield parents + (v,)


if __name__ == '__main__':
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(6) == 720
    for i in range(1, 5):
        assert len(list(permutation(list(range(i))))) == factorial(i)
        assert len(set(permutation(list(range(i))))) == factorial(i)
