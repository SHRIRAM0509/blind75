# https://leetcode.com/problems/word-search/


'''
* Stupid question - right answer sometimes will accept, sometimes won't
'''


from typing import List


def exist(board: List[List[str]], word: str) -> bool:
	num_rows, num_cols, word_len = len(board), len(board[0]), len(word)

	def is_valid(row, col, idx):
		return (
			0 <= row < num_rows
			and 0 <= col < num_cols
			and board[row][col] == word[idx]
		)

	def has_word(row, col, idx):
		if idx == word_len:
			return True

		if is_valid(row, col, idx):
			temp = board[row][col]
			board[row][col] = None
			found = (
				has_word(row+1, col, idx+1)
				or has_word(row-1, col, idx+1)
				or has_word(row, col+1, idx+1)
				or has_word(row, col-1, idx+1)
			)
			board[row][col] = temp
			return found

		return False

	for i in range(num_rows):
		for j in range(num_cols):
			if has_word(i, j, 0):
				return True
	return False


def main():
	board = [list(map(int, input(f"Enter row #{i}").split())) for i in range(
		int(input("Enter no of rows:")))]
	word = input()
	print(exist(board, word))


if __name__ == '__main__':
	main()
