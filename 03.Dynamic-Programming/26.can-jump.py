# https://leetcode.com/problems/jump-game/


'''
O(n^2) solution (very slow but passed tests):
	* dp[0] is True, So initializing dp with True
	* dp[i] = dp[j] and nums[j] >= i-j; until dp[i] becomes False
'''


from typing import List


def can_jump(nums: List[int]) -> bool:
	dp = [True]*len(nums)
	for i in range(1, len(nums)):
		for j in range(i-1, -1, -1):
			dp[i] = dp[j] and nums[j] >= i-j
			if dp[i]:
				break
	return dp[-1]


def main():
	nums = list(map(int, input().split()))
	print(can_jump(nums))


if __name__ == '__main__':
	main()
