# https://leetcode.com/problems/longest-substring-without-repeating-characters


'''
* Brute force takes O(n^2) with two loops fully iterated
* We can use a sliding window to find valid sub-strings using two pointers start & end
* Move end from 0 to n; set start to the index where repetition happens first
* To find the index where repetition happens first maintain a seen set
* Remove characters of s at i to repetition index from the seen set.
'''


def length_of_longest_substring(s: str) -> int:
	start, max_count, seen = 0, 0, set()

	for end, char in enumerate(s):
		while char in seen:
			seen.remove(s[start])
			start += 1
		seen.add(char)

		max_count = max(max_count, end-start+1)

	return max_count


def main():
	s = input()
	print(length_of_longest_substring(s))


if __name__ == '__main__':
	main()
