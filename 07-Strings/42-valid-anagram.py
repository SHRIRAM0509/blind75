# https://leetcode.com/problems/valid-anagram/


'''
Counter method:
	* Use collections' Counter to compare if count of characters in corresponding strings are the same
 
Normal method:
	* compare character counts
'''

from collections import Counter, defaultdict


def is_anagram_normal(s: str, t: str) -> bool:
	if len(s) != len(t):
		return False

	if s == t:
		return True

	s_counter, t_counter = defaultdict(int), defaultdict(int)
	for c1, c2 in zip(s, t):
		s_counter[c1] += 1
		t_counter[c2] += 1

	for k, v in s_counter.items():
		if v != t_counter[k]:
			return False

	return True


def is_anagram(s: str, t: str) -> bool:
	if len(s) != len(t):
		return False

	if s == t:
		return True

	s, t = Counter(s), Counter(t)

	for k, v in s.items():
		if v != t[k]:
			return False

	return True


def main():
	s, t = input().split()
	print(is_anagram(s, t))


if __name__ == '__main__':
	main()
