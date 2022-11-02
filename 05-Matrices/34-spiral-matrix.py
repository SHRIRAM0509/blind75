# https://leetcode.com/problems/spiral-matrix/

'''
* Idea is to have 4 pointers to define the 4 boundaries (left, right, top, bottom)
* Order of spiral is
	1. left -> right, with top fixed. Increment top
	2. top -> bottom, with right fixed. Decrement right
	3. right -> left, with bottom fixed. Decrement bottom
	4. bottom -> top, with left fixed. Increment left
* The above order goes on as long as top < bottom and left < right.
* Stop iteration after first two for loops if top == bottom or left == right
* Append the element accordingly to a res array
'''

from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
	res, top, left, right, bottom = [], 0, 0, len(matrix[0]), len(matrix)

	while top < bottom and left < right:
		for i in range(left, right):
			res.append(matrix[top][i])
		top += 1

		for i in range(top, bottom):
			res.append(matrix[i][right-1])
		right -= 1

		if left == right or top == bottom:
			break

		for i in range(right-1, left-1, -1):
			res.append(matrix[bottom-1][i])
		bottom -= 1

		for i in range(bottom-1, top-1, -1):
			res.append(matrix[i][left])
		left += 1

	return res


def main():
	matrix = [list(map(int, input(f"Enter row #{i}").split())) for i in range(
		int(input("Enter no of rows:")))]
	print(spiral_order(matrix))


if __name__ == '__main__':
	main()
