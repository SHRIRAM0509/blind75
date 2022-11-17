# https://leetcode.com/problems/longest-palindromic-substring/


'''
* Maintain a visited dict to store character indices
* Final solution takes O(n^2) time and O(n) space
'''


from collections import defaultdict


def longest_palindrome(s: str) -> str:
	visited = defaultdict(list)
	l, r, w_len = 0, 0, 0

	for i, ch in enumerate(s):
		for j in visited[ch]:
			if i-j > w_len:
				string = s[j:i+1]
				if string == string[::-1]: # update window if palindrome
					l, r = j, i
					w_len = i-j
			else: # no use in proceeding further in the loop
				break
		visited[ch].append(i)
	return s[l: r+1]


def main():
	print(longest_palindrome(input()))


if __name__ == '__main__':
	main()
