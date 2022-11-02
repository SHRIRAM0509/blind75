# https://leetcode.com/problems/search-in-rotated-sorted-array/

'''
* Task is to complete in O(log(n)) time
* Array is rotated towards right
* Recursion termination cases:
    1. if empty, return -1
    2. if target equals first or last return index
* Offset is used to find index in original list
'''

from typing import List


def search(nums: List[int], target: int, offset=0) -> int:
    if not nums:
        return -1
    if target == nums[0]:
        return 0 + offset
    if target == nums[-1]:
        return len(nums) - 1 + offset
    return search(nums[1:-1], target, offset + 1)


def main():
    nums: List[int] = list(map(int, input().split()))
    target: int = int(input())
    print(search(nums, target))


if __name__ == '__main__':
    main()
