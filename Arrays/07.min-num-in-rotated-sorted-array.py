# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

'''
* Task is to complete in O(log(n)) time
* Observations:
	1. Array is rotated towards right
	2. Generally first element > last element => we use this for recursion
	3. If last >= first, we can terminate recursion
'''

from typing import List


def find_min(nums: List[int], prev_min=float('inf')) -> int:
    if not nums:
        return prev_min

    first, last = nums[0], nums[-1]
    if last >= first:
        return min(first, prev_min)

    return find_min(nums[1:-1], last)


def main():
    nums: List[int] = list(map(int, input().split()))
    print(find_min(nums))


if __name__ == '__main__':
    main()
