'''

On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, 
and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase 
characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, 
west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, 
or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move 
into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.
'''

def rook_captures(board):
    captures = 0

    def rook_position():
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    return (i, j)

    i, j = rook_position()

    r, c = i - 1, j
    while r >= 0 and board[r][c] == '.': r -= 1
    if r > -1 and board[r][c] == 'p': captures += 1

    r, c = i + 1, j
    while r < len(board) and board[r][c] == '.': r += 1
    if r < len(board) and board[r][c] == 'p': captures += 1

    r, c = i, j - 1
    while c >= 0 and board[r][c] == '.': c -= 1
    if c > -1 and board[r][c] == 'p': captures += 1

    r, c = i, j + 1
    while c < len(board[0]) and board[r][c] == '.': c += 1
    if c < len(board) and board[r][c] == 'p': captures += 1

    return captures

