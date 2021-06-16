def solve(board, i, j):
	rows = len(board)
	columns = len(board[0])

	if i>=rows or i==columns or j<0:
		return

	if board[i][j]=='X':
		board[i][j]='O'
		solve(board, i, j+1)
		solve(board, i, j-1)
		solve(board, i+1, j)
		solve(board, i-1, j)

	return


def startingIndex(board):
	count = 0
	rows = len(board)
	columns = len(board[0])

	for i in range(rows):
		for j in range(columns):
			if board[i][j]=='X':
				count += 1
				solve(board, i, j)

	return count

if __name__ == '__main__':
	board = [['X','O','O','X','O','O','O'],['X','X','O','O','O','X','O'],['O','X','O','O','O','X','O']]
	print(startingIndex(board))