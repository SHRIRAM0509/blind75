# https://leetcode.com/problems/coin-change/

'''
Brute Force:-
* Takes O(mn) time, where m is the no of coins and n is the amount.

Top-down approach:-
* Takes O(n) Space
* Prunes visited sub trees
* Uses memoization with DFS

Bottom-up approach:-
* Takes O(mn) time, where m is the no of coins and n is the amount
* Occupies O(n) space.
* Uses DP
'''

from typing import List


def find_fewest_num_coins_dfs(coins: List[int], amount: int):
	memo = {}
	memo[0] = 0

	def dfs(coins: List[int], amount: int) -> int:
		if amount in memo:
			return memo[amount]
		if amount < 0:
			return float('inf')
		memo[amount] = min(1 + dfs(coins, amount-amt) for amt in coins)
		return memo[amount]

	count = dfs(coins, amount)
	return -1 if count == float('inf') else count


def find_fewest_num_coins(coins: List[int], amount: int) -> int:
	dp = [float('inf')] * (amount+1)
	dp[0] = 0

	for amt in range(1, amount+1):
		all_coin_counts_generator = (1 + dp[amt - coin_amt]
		                             for coin_amt in coins if amt - coin_amt >= 0)
		dp[amt] = min(all_coin_counts_generator, default=dp[amt])

	return -1 if dp[amount] == float('inf') else dp[amount]


def main():
	coins = list(map(int, input().split()))
	print(find_fewest_num_coins(coins))


if __name__ == '__main__':
	main()
