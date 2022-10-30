# https://leetcode.com/problems/rotate-image/


'''
Basic approach:
	* Store a copy of matrix to set the values in place
	* Final solution is O(n^2) time and O(n^2) space
'''


from copy import deepcopy
from typing import List


def rotate(self, matrix: List[List[int]]) -> None:
    """
	Do not return anything, modify matrix in-place instead.
	"""
    n, mat_copy = len(matrix), deepcopy(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = mat_copy[n-j-1][i]


def main():
	matrix = [list(map(int, input(f"Enter row #{i}").split())) for i in range(
		int(input("Enter no of rows:")))]
	print(rotate(matrix))


if __name__ == '__main__':
	main()
