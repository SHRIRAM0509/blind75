# https://leetcode.com/problems/house-robber/

'''
* Consecutive houses can't be used
* Doesn't mean alternate houses have to be used. Can skip houses
* Pattern: very similar to 0/1 knapsack with some logic to skip alternate houses
* Observations & Algo:
	1. first two houses always have same value in nums. Made sense to initialize dp with nums.
	2. starting outer loop i from 2 to n
	3. using inner loop from 0 to i-2 (skips i-1 as it can't be used) and picking max one
	4. at any point i, dp[i] gives max robbed money
	5. curr_max is needed to store temp max values as dp[i] couldn't be directly modified
* Final algo takes O(n^2) time and O(n) space
'''


from typing import List


def rob(nums: List[int]) -> int:
	dp = list(nums)
	for i in range(2, len(nums)):
		curr_max = dp[i-2]
		for j in range(i-2, -1, -1):
			curr_max = max(curr_max, dp[i] + dp[j])
		dp[i] = curr_max
	return max(dp)


def main():
	nums = list(map(int, input().split()))
	print(rob(nums))


if __name__ == '__main__':
	main()
