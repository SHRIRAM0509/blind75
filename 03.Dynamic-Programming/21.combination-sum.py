# https://leetcode.com/problems/combination-sum-iv/

'''
* Pattern similar to fibonacci, climbing stairs type problems
* Final DP solution takes O(n^2) time and O(n) space.
'''


from typing import List


def combination_sum_bottom_up(nums: List[int], target: int) -> int:
	memo = {}

	def aux(nums: List[int], target: int) -> int:
		if target == 0:
			return 1
		key = f"{nums}{target}"
		if key in memo:
			return memo[key]
		memo[key] = sum(aux(nums, target - num) for num in nums if target >= num)
		return memo[key]
	return aux(nums, target)


def combination_sum4(nums: List[int], target: int) -> int:
	dp = [0]*(target+1)
	dp[0] = 1 # 0 is not in test case; just to facilitate
	dp[1] = int(1 in nums) # check if 1 in nums 

	for i in range(2, target+1):
		for num in nums:
			if i >= num:
				dp[i] += dp[i-num]
	return dp[target]


def main():
	nums = list(map(int, input().split()))
	target = int(input())
	print(combination_sum4(nums, target))


if __name__ == '__main__':
	main()
