# https://leetcode.com/problems/longest-increasing-subsequence/


'''
* Eg: nums = [10,9,2,5,3,7,101,18] => Answer is 4; [2,3,7,101] or [2, 5, 7, 18] or...
* Always first element has length 1. So, we can initialize dp list with 1.
* This is a 0/1 knapsack type problem. You include an element or exclude it.
* Idea is to keep moving i for each element, from 0 to i find the LIS till that point (sub problem).
* To move i needs one loop and to go back and check LIS from 0 to i another loop is needed.
'''


from typing import List


def length_of_lis(nums: List[int]) -> int:
	dp = [1]*len(nums)
	for i in range(1, len(nums)):
		for j in range(0, i):
			if nums[j] < nums[i]:  # increasing subsequence
				dp[i] = max(dp[i], dp[j] + 1)  # include or exclude - 0/1 knapsack
	return max(dp)


def main():
	nums = list(map(int, input().split()))
	print(length_of_lis(nums))


if __name__ == '__main__':
	main()
