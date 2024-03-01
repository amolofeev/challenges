"""
Слияние пересечений интервалов

Дано:
массив интервалов [[lower bound, upper bound], ...], где lower bound <= upper bound

[[8,10], [1,3], [2,6],  [15, 17]]

Надо:
Объединить пересекающиеся диапазоны

[[1,6], [8, 10], [15, 17]]

"""


class Interval(list):
    """
    Вспомогательный класс-обертка над list для возможности сортировать более, чем по 1 ключу
    + сахар для удобства
    """
    def __lt__(self, other: 'Interval'):
        """
        Сортируем lower.asc & upped.desc
        [
            [1,3], [1,2], [1,1],
            [2,3], [2, 2]
            [5,5],
        ]
        таким образом из каждой "строки" нам нужен только 1й элемент
        слияние или результат будет происходить только при переходе на след "строку"
        """
        return (
                (self.lower == other.lower and self.upper > other.upper) or
                self.lower < other.lower
        )
    
    @property
    def lower(self) -> int:
        return self[0]

    def _set_upper(self, value: int):
        self[1] = value

    def _get_upper(self) -> int:
        return self[1]

    upper = property(_get_upper, _set_upper)

    def test(self, other: 'Interval') -> int:
        if self.lower <= other.lower <= self.upper >= other.upper:
            # полное поглощение
            return -1
        elif (self.lower <= other.lower <= self.upper) and (self.upper < other.upper):
            # пересечение с расширением в право
            return 0
        else:
            # не пересеклись
            return 1


def merge_intervals(intervals: list[Interval]) -> list[Interval]:
    """
    >>> merge_intervals([Interval([1,1])])
    [[1, 1]]
    >>> merge_intervals([Interval([1,1]), Interval([1,1])])
    [[1, 1]]
    >>> merge_intervals([Interval([1,1]), Interval([1,2])])
    [[1, 2]]
    >>> merge_intervals([Interval([2,3]), Interval([1,2])])
    [[1, 3]]
    >>> merge_intervals([Interval([2,3]), Interval([1,2]), Interval([5,5])])
    [[1, 3], [5, 5]]
    >>> merge_intervals([Interval([2,3]), Interval([1,2]), Interval([5,9]), Interval([5,5])])
    [[1, 3], [5, 9]]
    """
    intervals = sorted(intervals)
    result = []
    current = intervals.pop(0)
    for i in intervals:
        match current.test(i):
            case -1:
                pass
            case 0:
                current.upper = i.upper
            case 1:
                result.append(current)
                current = i
    result.append(current)
    return result
