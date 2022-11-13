# https://leetcode.com/problems/group-anagrams/


'''
* anagrams when sorted provide same result
* Final solution takes O(n) time and O(n) space
'''


from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
	res = defaultdict(list)
	for s in strs:
		res[tuple(sorted(s))].append(s)
	return res.values()


def main():
	print(group_anagrams(input().split()))


if __name__ == '__main__':
	main()
