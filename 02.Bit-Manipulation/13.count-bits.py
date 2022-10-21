# https://leetcode.com/problems/counting-bits/


'''
* Brute force takes O(n^2) time
* Key Ideas:
	1. i & i-1 is 0 if, i is a power of 2.
	2. We can utilize previous results by finding i ^ last_power_of_2. 
 	3. Eg. 110 ^ 100 is 010. So count of 110 is (1 + count(010)). 1 is because always powers of 2 always have bit count 1.
* This DP solution takes O(n) time and O(n) space complexity
'''

from typing import List


def count_bits(n: int) -> List[int]:
	bit_count = [0]*(n+1)
	last_power_of_2 = 0
	for i in range(1, n+1):
		power_of_2 = (i & (i-1)) == 0
		if power_of_2:
			last_power_of_2 = i
			bit_count[i] = 1
		else:
			bit_count[i] = 1 + bit_count[last_power_of_2 ^ i]
	return bit_count


def main():
	n = int(input())
	print(count_bits(n))


if __name__ == '__main__':
	main()
