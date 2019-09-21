from typing import Generator, Iterable, Callable, Union


def filter_(fn: Union[None, Callable], iter_: Iterable) -> Generator:
    for i in iter_:
        if fn is None and i:
            yield i
        elif fn:
            tmp = fn(i)
            if tmp:
                yield i


if __name__ == '__main__':
    fn = lambda x: x - 1
    assert list(filter(fn, range(5))) == list(filter(fn, range(5))) == [0, 2, 3, 4]
    assert list(filter(None, range(5))) == list(filter(None, range(5))) == [1, 2, 3, 4]
