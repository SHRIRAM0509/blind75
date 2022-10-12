# https://leetcode.com/problems/product-of-array-except-self/

'''
* Division cannot be used
* Idea is to accumulate products in forward and backward directions
* So, prod_except_self[i] = forward[i-1] * backward[i+1]
* Two n sized lists needs to be stored for forward and backward accumulation. Instead, we're cutting it down and using one list to solve it.
* Final solution needs O(n) time and O(n) space complexity, i.e. O(1) additional space complexity.
'''

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    # taking a copy of nums
	result, last_idx = list(nums), len(nums)-1

    # forward accumulation
	curr_prod = 1
	for i in range(last_idx):
		result[i] *= curr_prod
		curr_prod *= nums[i]

	# result[i] = forward[i-1] * backward[i+1]; where backward[i+1] is curr_prod and forward[i-1] is result[i-1]
	curr_prod = 1
	for i in range(last_idx, 0, -1):
		result[i] = result[i-1] * curr_prod
		curr_prod *= nums[i]
	# directly setting value because result[i-1] at i=0 doesn't exist
	result[0] = curr_prod

	return result


def main():
    nums: List[int] = list(map(int, input().split()))
    print(product_except_self(nums))


if __name__ == '__main__':
    main()
