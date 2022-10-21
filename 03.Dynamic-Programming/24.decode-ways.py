# https://leetcode.com/problems/decode-ways/


'''
* If a string starts with 0 return 0
* An integer string is valid if first char is not zero and integer is between 1 and 26
* Take 226, we can create sub problem in this way
	f(226) = (f(22) if 6 is valid) + (f(2) if 26 is valid)
* So, at any point for string s, f(i) = (f(i-1) if s[i] is valid) + (f[i-2] if s[i-1:i+1] is valid)
* Final solution takes O(n) time and O(n) space
'''


def is_valid(s: str) -> bool:
	return 1 <= int(s) <= 26 and s[0] != '0'


def num_decodings(s: str) -> int:

	if s[0] == '0':
		return 0

	dp = [1]*len(s)

	for i in range(1, len(s)):
		valid_last_digit = is_valid(s[i])
		valid_two_digit_num = is_valid(s[i-1:i+1])
		dp[i] = (valid_last_digit and dp[i-1]) + (valid_two_digit_num and dp[i-2])
	return dp[-1]


def main():
	s = input()
	print(num_decodings(s))


if __name__ == '__main__':
	main()
