# https://leetcode.com/problems/valid-palindrome/

'''
* Clean characters and just check if reverse is same as original.
* Final solution takes O(n) time and constant space.
'''


def is_palindrome(s: str) -> bool:
	sanitized_s = ''.join(ch for ch in s.lower() if ch.isalnum())
	return sanitized_s == sanitized_s[::-1]


def main():
	print(is_palindrome(input()))


if __name__ == '__main__':
	main()
