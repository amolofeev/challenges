"""
https://en.wikipedia.org/wiki/Bubble_sort
"""


def bubble_sort(iter_, reverse=False):
    copy = list(iter_)  # actually i could sort inplace without extra memory usage
    length = len(copy)
    for i in range(length):
        for j in range(length):
            if not reverse and copy[i] < copy[j]:
                copy[i], copy[j] = copy[j], copy[i]
            elif reverse and copy[i] > copy[j]:
                copy[i], copy[j] = copy[j], copy[i]
    return copy


if __name__ == '__main__':
    assert bubble_sort([3, 2, 1, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([3, 2, 1, 4, 5], reverse=True) == [5, 4, 3, 2, 1]
