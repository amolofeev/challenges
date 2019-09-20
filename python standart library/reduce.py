from typing import Any, Callable, Iterable


def reduce(fn: Callable, iter_: Iterable, initial: Any) -> Any:
    for i in iter_:
        initial = fn(initial, i)
    return initial


if __name__ == '__main__':
    # factorial
    assert reduce(lambda old, new: old * new, range(1, 5), 1) == 24
    assert reduce(lambda old, new: old * new, range(1, 6), 1) == 120
