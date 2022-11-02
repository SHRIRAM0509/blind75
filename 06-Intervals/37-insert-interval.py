from typing import List
from functools import reduce

from Interval import Interval


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    if not intervals:
        return [new_interval]

    intervals: List[Interval] = [Interval.from_list(
        interval) for interval in intervals]
    new_interval: Interval = Interval.from_list(new_interval)

    def reducer(a: Interval, b: Interval, acc):
        if not acc:
            return a.merge(b)
        *rest, b = acc
        rest.extend(a.merge(b))
        return rest

    intervals = reduce(lambda acc, x: reducer(
        x, new_interval, acc), intervals, [])

    return [interval.to_list() for interval in intervals]


def main():
    # intervals: List[List[int]] = [list(map(int, input(f"Enter interval #{i}").split())) for i in range(
    #     int(input("Enter no of rows:")))]
    # new_interval: List[int] = list(map(int, input().split()))
    print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))


if __name__ == '__main__':
    main()
