# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

'''
* Brute force needs O(n^2) to find max profit
* Pattern is to use a double pointer
* Aim to find something increasing
* So, 
	let i = 0, j = 1
	if a[j] > a[i] -> move j one step ahead
	else, set i = j,  move j one step ahead (incrementing i is useless as the curve was decreasing, so directly setting i to j)
* update max profit if curr profit (a[j] - a[i]) is greater than it
* Final -> O(n) time, O(1) space 
'''

from typing import List


def find_best_stock_sell_time(prices: List[int]) -> int:
	i, j = 0, 1
	max_profit = -float('inf')
	no_of_days = len(prices)

	while j < no_of_days:
		curr_profit = prices[j] - prices[i]

		if curr_profit > max_profit:
			max_profit = curr_profit

		# if curr_profit < 0, i.e. a[j] < a[i], then curve is decreasing
		if curr_profit < 0:
			i = j

		# always keep moving j one step ahead
		j += 1

	# handle one element in array case, no profit case
	return max_profit if max_profit > 0 else 0


def main():
	prices = list(map(int, input().split()))
	print(find_best_stock_sell_time(prices))


if __name__ == '__main__':
	main()
