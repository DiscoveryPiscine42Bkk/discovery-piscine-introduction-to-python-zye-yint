
def checkmate(board_string):
    board = [list(row) for row in board_string.strip().split('\n')]
    size = len(board)
    
    # Find King's position
    king_pos = None
    for y in range(size):
        for x in range(len(board[y])):
            if board[y][x] == 'K':
                king_pos = (y, x)
                break
        if king_pos:
            break

    if not king_pos:
        print("Fail")  # No king = auto-fail
        return

    def in_bounds(y, x):
        return 0 <= y < size and 0 <= x < len(board[y])

    def is_clear_path(y, x, dy, dx):
        y += dy
        x += dx
        while in_bounds(y, x):
            if board[y][x] == '.':
                y += dy
                x += dx
                continue
            return (y, x)
        return None

    yk, xk = king_pos

    # Check for Pawn threats (assuming pawns attack from bottom to top)
    for dy, dx in [(-1, -1), (-1, 1)]:
        yp, xp = yk + dy, xk + dx
        if in_bounds(yp, xp) and board[yp][xp] == 'P':
            print("Success")
            return

    # Check for Rook or Queen in straight lines
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        found = is_clear_path(yk, xk, dy, dx)
        if found:
            fy, fx = found
            if board[fy][fx] in ('R', 'Q'):
                print("Success")
                return

    # Check for Bishop or Queen in diagonals
    for dy, dx in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        found = is_clear_path(yk, xk, dy, dx)
        if found:
            fy, fx = found
            if board[fy][fx] in ('B', 'Q'):
                print("Success")
                return

    print("Fail")
