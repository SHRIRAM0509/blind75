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


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
	if not intervals:
		return 0

	intervals.sort(key=lambda x:(x[1],x[0]))
	count, curr_end = 0, intervals[0][1]
	for start, end in intervals[1:]:
		if start >= curr_end:
			curr_end = end
		else:
			count += 1
	return count


def erase_overlap_intervals_with_class(intervals: List[List[int]]) -> int:
	if len(intervals) <= 1:
		return 0

	intervals: List[Interval] = [Interval(
		interval) for interval in sorted(intervals, key=lambda x: (x[1], x[0]))]
	count = 0
	curr = intervals[0]
	for i in intervals[1:]:
		if i >= curr: # different meaning given to >= check class
			curr = i
		else:
			count += 1
	return count


def main():
    intervals: List[List[int]] = [list(map(int, input(f"Enter interval #{i}").split())) for i in range(
        int(input("Enter no of rows:")))]
    print(erase_overlap_intervals(intervals))


if __name__ == '__main__':
    main()
