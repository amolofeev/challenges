def zip_(*iterables):
    iterators = tuple(map(iter, iterables))
    while True:
        try:
            yield tuple(next(i) for i in iterators)
        except RuntimeError:
            break


if __name__ == '__main__':
    assert list(zip_(range(3), range(4))) == list(zip(range(3), range(4)))
