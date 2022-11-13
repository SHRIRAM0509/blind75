# https://leetcode.com/problems/minimum-window-substring/


'''
* Cannot use a set to compare s and t. t contains duplicates. So, using a dict to store character counts of t (t_counter).
* Maintain have - sum of character counts to fulfil t, need - character count sum in t
* left and right denote the two ends of the sliding window. min_window stores the min window
* store character counts of s if it's in t (even if it repeats in s) using s_counter
* At some point when have == need (this means s[left: right+1] contains t)
	if left is in t:
		update window
		decrement have
		decrement s_counter (because we also added repeats so always s_counter[s[left]] >= t_counter[s[left]])
	keep updating left till have != need
* min_window will give the answer
* Final solution is O(n) time and takes O(n) space (actually it depends on characters in s and t).
'''


from collections import defaultdict


def min_window(s: str, t: str) -> str:
	t_counter, s_counter = defaultdict(int), defaultdict(int)
	min_window, min_window_len = (), float('inf')
	left, have, need = 0, 0, 0

	for ch in t:
		t_counter[ch] = t_counter[ch] + 1
		need += 1

	for right, ch in enumerate(s):
		if ch in t_counter:
			s_counter[ch] = s_counter[ch] + 1
			have += s_counter[ch] <= t_counter[ch]

			while have == need:
				if s[left] in t_counter:
					have -= s_counter[s[left]] == t_counter[s[left]]
					s_counter[s[left]] -= 1

					if (right-left+1) < min_window_len:
						min_window_len = right-left+1
						min_window = (left, right+1)

				left += 1

	return s[slice(*min_window)] if min_window else ""
