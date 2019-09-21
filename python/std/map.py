from typing import Callable, Iterable, Generator


def map_(fn: Callable, iter_: Iterable) -> Generator:
    for i in iter_:
        yield fn(i)


if __name__ == '__main__':
    fn = lambda x: x+1
    assert list(map_(fn, range(5))) == list(map(fn, range(5)))
