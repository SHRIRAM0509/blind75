# https://leetcode.com/problems/valid-parentheses/


'''
* Use a stack to check matching brackets/
* Final solution takes O(n) time and space.
'''


def is_valid(s: str) -> bool:
	pairs = {
		'(': ')',
		'{': '}',
		'[': ']'
	}

	stack = []
	for br in s:
		if br in pairs:
			stack.append(br)
			continue

		if not stack:
			return False

		if br != pairs[stack.pop()]:
			return False

	return not stack


def main():
	print(is_valid(input()))


if __name__ == '__main__':
	main()
