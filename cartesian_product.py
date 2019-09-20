"""
https://en.wikipedia.org/wiki/Cartesian_product

    1  2   3
  ------------
A| A1  A2  A3
B| B1  B2  B3
C| C1  C2  C3
D| D1  D2  D3
"""
import itertools
from typing import Generator, Tuple, Optional, Any


def odometer(*iterables, values: Optional[Tuple[Any, ...]] = None) -> Generator:
    values = values or ()
    if iterables:
        for i in iterables[0]:
            if iterables[1:]:
                yield from odometer(*iterables[1:], values=values + (i,))
            else:
                yield values + (i,)
    else:
        yield ()


def cartesian_product(*iterables, repeat: int = 1) -> Generator:
    yield from odometer(*(iterables * repeat))


if __name__ == '__main__':
    assert list(cartesian_product('ab', (1, 2,))) == list(itertools.product('ab', (1, 2)))
    assert list(cartesian_product('ab', (1, 2,), repeat=2)) == list(itertools.product('ab', (1, 2), repeat=2))
    assert list(cartesian_product('ab', (1, 2,), repeat=0)) == list(itertools.product('ab', (1, 2), repeat=0))
