# https://leetcode.com/problems/insert-interval/


'''
* Convert lists to intervals
* Use a reduce function to merge intervals
* Takes O(n) time and O(1) extra space
'''


from typing import List
from functools import reduce

from Interval import Interval


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    if not intervals:
        return [new_interval]

    intervals: List[Interval] = [Interval.from_list(
        interval) for interval in intervals]
    new_interval: Interval = Interval.from_list(new_interval)

    def reducer(acc: List[Interval], i: Interval):
        if not acc:
            return i.merge(new_interval) # merge might return one/two intervals depending on whether they overlap

        # acc.pop() removes and returns last element
        acc.extend(i.merge(acc.pop()))
        return acc

    return [interval.to_list() for interval in reduce(reducer, intervals, [])]


def main():
    intervals: List[List[int]] = [list(map(int, input(f"Enter interval #{i}").split())) for i in range(
        int(input("Enter no of rows:")))]
    new_interval: List[int] = list(map(int, input().split()))
    print(insert(intervals, new_interval))


if __name__ == '__main__':
    main()
