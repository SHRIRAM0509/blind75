# https://leetcode.com/problems/house-robber-ii/


'''
* Houses are in a circular fashion.
* So, rob2(x) = max( rob1(x[1:]), rob1(x[:-1] )
* Final algo takes O(n^2) time and O(n) space
'''


from typing import List


def rob1(nums: List[int]) -> int:
	dp = list(nums)
	for i in range(2, len(nums)):
		curr_max = dp[i-2]
		for j in range(i-2, -1, -1):
			curr_max = max(curr_max, dp[i] + dp[j])
		dp[i] = curr_max
	return max(dp)


# refer Dynamic-Programming/22.house-robber.py
def rob2(nums: List[int]) -> int:
	if len(nums) == 1:
		return nums[0]
	return max(rob1(nums[:-1]), rob1(nums[1:]))


def main():
	nums = list(map(int, input().split()))
	print(rob2(nums))


if __name__ == '__main__':
	main()
