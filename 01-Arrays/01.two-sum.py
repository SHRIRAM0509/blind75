# https://leetcode.com/problems/two-sum

'''
* Brute force solution requires O(n^2)
* Use a lookup dictionary to maintain previous results and check if diff is there in lookup
* Final - O(n) time, O(n) space
'''


from typing import Dict, List


def get_two_addends(nums, target) -> List[int]:
	lookup: Dict[int, int] = {}
	for idx, num in enumerate(nums):
		diff = target - num
		if diff in lookup:
			return [lookup[diff], idx]
		lookup[num] = idx
	else:
		raise Exception(f"No two nos in array add up to {target}")


def main():
	nums = list(map(int, input().split()))
	target = int(input())
	print(get_two_addends(nums, target))


'''
test_cases = [
	([2,7,11,15], 9), #normal case - [0,1]
	([3,2,4], 6), #check if 3 same number isn't counted twice - [1,2]
	([3,3], 6), #duplicates check - [0,1]
	([2,3], 1), #no matches
	([4, 2, -1, 5], 3) #check for negative nos - [0,3]
]
'''


if __name__ == '__main__':
	main()
