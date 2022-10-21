# https://leetcode.com/problems/3sum/

'''
* Brute force O(n^3)
* If a + b + c = 0, then b + c = -a
* Idea is to use two sum logic inside a for loop with target as -a.
* Final time complexity is O(n^2)
* Sorting it to avoid repetition of the triplets
'''

from typing import List, Set


def three_sum(nums: List[int]) -> List[List[int]]:
    triplets = set()
    nums = sorted(nums)
    for idx, num in enumerate(nums):
        target = -1 * num
        lookup: Set[int] = set()
        for numb in nums[idx+1:]:
            diff = target - numb
            if diff in lookup:
                triplets.add((num, diff, numb))
            lookup.add(numb)
    return list(triplets)


def main():
    nums: List[int] = list(map(int, input().split()))
    print(three_sum(nums))


if __name__ == '__main__':
    main()
