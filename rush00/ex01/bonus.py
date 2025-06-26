
import sys
from checkmate import checkmate

def is_valid_board(lines):
    length = len(lines[0])
    return all(len(line) == length for line in lines)

def read_board_file(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
            if not lines or not is_valid_board(lines):
                print("Error")
                return
            board = '\n'.join(lines)
            checkmate(board)
    except:
        print("Error")

def main():
    for file_path in sys.argv[1:]:
        read_board_file(file_path)

if __name__ == "__main__":
    main()
