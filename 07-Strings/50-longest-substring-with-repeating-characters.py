# https://leetcode.com/problems/longest-repeating-character-replacement


'''
* Using sliding window technique with left and right pointers being the ends of the window
* The idea is in a window, find the most repeating character. If window_size - max_char_count <= k, then it's a valid window.
* s_counter maintains the count of characters in the window.
* Final solution takes O(nm) time and O(n) space, where m is the no of unique characters in the string (0 < m <= 26).
* There is a much optimal solution with O(n) time. Refer https://www.youtube.com/watch?v=gqXU1UyA8pk&t=486s
'''


from collections import defaultdict


def character_replacement(s: str, k: int) -> int:
	left, max_window, s_counter = 0, 0, defaultdict(int)

	for right, ch in enumerate(s):
		s_counter[ch] += 1
		curr_window_size = right - left + 1

		if curr_window_size - max(s_counter.values()) <= k:
			max_window = max(max_window, curr_window_size)
		else:
			s_counter[s[left]] -= 1
			left += 1

	return max_window


def main():
	s, k = input().split()
	print(character_replacement(s, int(k)))


if __name__ == '__main__':
	main()
