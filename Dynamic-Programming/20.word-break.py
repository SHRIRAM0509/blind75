# https://leetcode.com/problems/word-break/


'''
* Using a dict for word lookup. Also, reusing the same for memoization also by initializing words in dict as true.
* Offset is the no of character from beginning. Eg. "hello" with offset 2 is "hel"
* if s[:offset+1] is in memo and is a valid word (memo[s[:offset+1]] = True), then check if f(s[offset+1:]) is True
* To handle other cases like if s = "applesanddog", s[:offset+1] is apple, but we want apples. So, or-ing with f(s, offset+1)
* Termination cases for recursion:
	1. string is in memo (could be True or False)
	2. if offset is same as length of string (this means string is not in dict at all - False)
'''


from collections import defaultdict
from typing import List


def word_break(s: str, wordDict: List[str]) -> bool:
	memo = defaultdict(lambda: False, {word: True for word in wordDict})

	def dfs(s, offset=0):
		if s in memo:
			return memo[s]

		offset += 1

		if offset == len(s):
			memo[s] = False
		else:
			memo[s] = (memo[s[:offset]] and dfs(s[offset:])) or dfs(s, offset)
		return memo[s]

	return dfs(s)


def main():
	s = input()
	word_dict = input().split()
	print(word_break(s, word_dict))


if __name__ == '__main__':
	main()
