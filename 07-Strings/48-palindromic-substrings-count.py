# https://leetcode.com/problems/palindromic-substrings/


'''
* Brute force takes O(n^2)
* Dynamic programming solution needs a dp array and a visited dict to store indices of characters
* dp[i] gives no of palindromic sub strings till i
* So, always dp[i] will minimum be equal to dp[i-1] + 1 (because repetition also counts)
* for j in visited[ch]
	if s[j] == ch and s[j:i+1] is a palindrome:
		increment dp[i] which was already set to (dp[i-1] + 1) in prev step
* Solution can be improved by storing indices of every  in visited instead of looping every time.
* Final solution is also O(n^2) but efficient and takes O(2n) space
'''


from collections import defaultdict


def count_substrings(s: str) -> int:
	size = len(s)
	visited, dp = defaultdict(list), [0]*size

	for i, ch in enumerate(s):
		dp[i] = dp[i-1] + 1

		for j in visited[ch]:
			string = s[j:i+1]
			dp[i] += (string == string[::-1])
		
		visited[ch].append(i)
	return dp[-1]


def main():
	print(count_substrings(input()))


if __name__ == '__main__':
	main()
