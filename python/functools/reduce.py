from typing import Any, Callable, Iterable


def reduce_(fn: Callable, iter_: Iterable, initial: Any) -> Any:
    for i in iter_:
        initial = fn(initial, i)
    return initial


if __name__ == '__main__':
    # factorial
    from functools import reduce

    fn = lambda old, new: old * new
    assert reduce_(fn, range(1, 5), 1) == reduce(fn, range(1, 5), 1) == 24
    assert reduce_(fn, range(1, 6), 1) == reduce(fn, range(1, 6), 1) == 120
