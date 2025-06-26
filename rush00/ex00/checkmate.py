#!/usr/bin/env python3
def is_king_attacked(board_str):
    grid = build_board(board_str)
    n = len(grid)

    if not all(len(row) == n for row in grid):
        print("Error")
        return

    for row in range(n):
        for col in range(n):
            piece = grid[row][col]
            if piece is None:
                continue

            attacks = find_attacks(piece, row, col, grid)
            for x, y in attacks:
                if grid[x][y] == 'K':
                    print("Success")
                    return
    print("Error")


def build_board(board_str):
    rows = board_str.strip().splitlines()
    return [[char if char != '.' else None for char in row.strip()] for row in rows]


def find_attacks(piece, x, y, board):
    if piece == 'P':
        return pawn_attacks(x, y, board)
    if piece == 'B':
        return sliding_attacks(x, y, board, [(-1, -1), (-1, 1), (1, -1), (1, 1)])
    if piece == 'R':
        return sliding_attacks(x, y, board, [(-1, 0), (1, 0), (0, -1), (0, 1)])
    if piece == 'Q':
        return sliding_attacks(x, y, board, [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)])
    return []


def pawn_attacks(x, y, board):
    targets = []
    if x > 0:
        if y > 0:
            targets.append((x - 1, y - 1))
        if y < len(board[0]) - 1:
            targets.append((x - 1, y + 1))
    return targets


def sliding_attacks(x, y, board, directions):
    n = len(board)
    attacks = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        while 0 <= nx < n and 0 <= ny < n:
            attacks.append((nx, ny))
            if board[nx][ny] is not None:
                break
            nx += dx
            ny += dy
    return attacks
