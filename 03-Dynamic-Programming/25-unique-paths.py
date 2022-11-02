# https://leetcode.com/problems/unique-paths/


'''
* initializing 2d array with 1 because first row and first column will all be 1
* f(i, j) = f(i-1, j) + f(i, j-1)
* Final solution takes O(n^2) time and space.
'''


def unique_paths(m: int, n: int) -> int:
	dp = [[1]*n]*m

	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = dp[i-1][j] + dp[i][j-1]
	return dp[-1][-1]


def main():
	m = int(input())
	n = int(input())
	print(unique_paths(m, n))


if __name__ == '__main__':
	main()
