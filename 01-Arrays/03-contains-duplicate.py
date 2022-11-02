# https://leetcode.com/problems/contains-duplicate/

'''
* Brute force takes O(n^2)
* Use a set to check contains, instead of a dictionary
* Final -> O(n) time, O(n) space
* If O(1) space complexity solution is asked, sort the array and check for duplicates.
'''

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    lookup = set()
    for num in nums:
        if num in lookup:
            return True
        lookup.add(num)
    return False


# For O(1) space complexity
def contains_duplicate_sorting(nums: List[int]) -> bool:
    sorted_nums = sorted(nums)
    prev_num = sorted_nums[0]
    for num in sorted_nums[1:]:
        if num == prev_num:
            return True
    return False


def main():
    nums = list(map(int, input().split()))
    print(contains_duplicate(nums))
