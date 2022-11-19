# https://leetcode.com/problems/top-k-frequent-elements/


'''
* Use a counter to find counts
* Use heapq's nlargest to find the k frequent elements
* Final solution takes O(k*logn) time and O(n) space
'''


from typing import List
from collections import Counter
from heapq import nlargest


def top_k_frequent(nums: List[int], k: int) -> List[int]:
	counter = Counter(nums)
	heap = (item[::-1] for item in counter.items())
	return [num for _, num in nlargest(k, heap)]


def main():
	nums = list(map(int, input().split()))
	k = int(input())
	print(top_k_frequent(nums, k))


if __name__ == '__main__':
	main()
