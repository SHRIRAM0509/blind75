# https://leetcode.com/problems/maximum-subarray/

'''
* Brute force takes O(n^3)
* Idea is to not use negative sums.
	1. A problem [-1, 2, 3] gives same result as [2, 3]. 
	2. [2, -3, 4, 1] is same as [4, 1] as effectively [2, -3] together is -1
* So, if curr_sum is negative, make it zero. Update max_sum if curr_sum > max_sum
* This handles all negative number case also.
* Also called as Kadane's algorithm
'''

from typing import List


def max_sub_array(nums: List[int]) -> int:
	max_sum, curr_sum = -float('inf'), 0

	for num in nums:
		if curr_sum < 0:  # to remove negative sums
			curr_sum = 0
		curr_sum += num
		max_sum = max(max_sum, curr_sum)
	return max_sum


def main():
    nums: List[int] = list(map(int, input().split()))
    print(max_sub_array(nums))


if __name__ == '__main__':
    main()
