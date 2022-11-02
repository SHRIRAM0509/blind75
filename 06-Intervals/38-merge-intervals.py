# https://leetcode.com/problems/merge-intervals


'''
* Brute force takes O(n^2) time
* Sort intervals by their start
* Convert lists to intervals
* Use a reduce function to merge intervals
* Takes O(n^logn) time and O(1) extra space
'''


from typing import List
from functools import reduce

from Interval import Interval


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals, key=lambda x: x[0])
    intervals: List[Interval] = [Interval(
        interval) for interval in intervals]

    def reducer(acc: List[Interval], i: Interval):
        if not acc:
            return [i]
        acc.extend(i.merge(acc.pop()))
        return acc

    return [interval.to_list() for interval in reduce(reducer, intervals, [])]


def main():
    intervals: List[List[int]] = [list(map(int, input(f"Enter interval #{i}").split())) for i in range(
        int(input("Enter no of rows:")))]
    print(merge(intervals))


if __name__ == '__main__':
    main()
