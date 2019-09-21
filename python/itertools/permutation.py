"""
https://en.wikipedia.org/wiki/Permutation

Recursion + generators.

Not fully equal to itertools.permutations because of current algorithm always generates full length series,
but itertools is able to generate series limited by length
# TODO: make fully equal to itertools.permutations
# TODO: remove recursion
"""


def permutations(in_, parents=None):
    parents = parents or ()
    for i in range(len(in_)):
        new_in = in_[:]
        v = new_in[i]
        del new_in[i]
        if new_in:
            yield from permutations(new_in, parents + (v,))
        else:
            yield parents + (v,)


if __name__ == '__main__':
    import itertools
    assert list(permutations([1, 2, 3])) == list(itertools.permutations([1, 2, 3]))
    assert list(permutations([1, 2, 3, 4])) == list(itertools.permutations([1, 2, 3, 4]))
