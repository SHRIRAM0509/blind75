# https://leetcode.com/problems/set-matrix-zeroes/


'''
* Rows can be set as zeroes easily without any loop
* Columns are tougher. So, it has to be maintained. We need a j_set
* Final solution is O(nm) time and O(m) time
'''


from typing import List


def set_zeroes(matrix: List[List[int]]) -> None:
	"""
	Do not return anything, modify matrix in-place instead.
	"""
	m, n = len(matrix), len(matrix[0])
	j_set = set()

	for i in range(m):
		flag = False
		for j in range(n):
			if matrix[i][j] == 0:
				j_set.add(j)
				flag = True
		if flag:  # set row as 0, after j has been captured
			matrix[i] = [0]*n

	for j in j_set:
		for i in range(m):
			matrix[i][j] = 0


def main():
	matrix = [list(map(int, input(f"Enter row #{i}").split())) for i in range(
		int(input("Enter no of rows:")))]
	print(set_zeroes(matrix))


if __name__ == '__main__':
	main()
