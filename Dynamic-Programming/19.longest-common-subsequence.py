# https://leetcode.com/problems/longest-common-subsequence/


'''
* Assuming ab;c and abd;c are the words (semi colon indicates current position of i and j resp.)
* if curr characters are equal -> lcs(abc, abdc) = lcs(ab, abd) + 1 
* else it's max of left cell or top cell
* Final solution takes O(n^2) time and space
'''


def longest_common_subsequence(text1: str, text2: str) -> int:
	# padding one top and left columns with 0 to make lookup easier
	dp = [[0 for _ in range(len(text2) + 1)] for c2 in range(len(text1) + 1)]

	for i, c1 in enumerate(text1, 1):
		for j, c2 in enumerate(text2, 1):
			if c1 == c2:
				dp[i][j] = dp[i-1][j-1] + 1
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])

	return dp[i][j]
