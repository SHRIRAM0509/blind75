# https://leetcode.com/problems/missing-number/

'''
* XOR properties:
	1. a ^ a = 0
	2. a ^ 0 = a
* So, we know the range [0, n], XOR them all. SO, rangeXOR => 0 ^ 1 ^ .. ^ n
* XOR the result of range rangeXOR with the nums in array.
* Repeating numbers should cancel out and missing number should come
* Alternate solution is to subtract all nums from sum of n natural nos. 
* Sum of n natural nos is n * (n+1) / 2. 
'''

from typing import List
from math import ceil


def missing_number_with_sum(nums: List[int]) -> int:
    len_nums = len(nums)
    sum_n_natural_nos = (1 + len_nums) * len_nums // 2
    for num in nums:
        sum_n_natural_nos -= num
    return sum_n_natural_nos


def missing_number(nums: List[int]) -> int:
	missing_num = 0
	for i in range(1, len(nums)+1):
		missing_num ^= i
	for num in nums:
		missing_num ^= num
	return missing_num


def main():
	nums = map(int, input().split())
	print(missing_number(nums))


if __name__ == '__main__':
	main()
