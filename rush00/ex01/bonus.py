import sys
from checkmate import is_king_attacked  # <-- use the correct function name

def main():
    if len(sys.argv) < 2:
        print("Usage: python bonus.py <board_file1> [<board_file2> ...]")
        return

    files = sys.argv[1:]
    for file in files:
        print(f"\nChecking board from file: {file}")
        try:
            with open(file, 'r') as f:
                board = f.read()
                is_king_attacked(board)  # call your logic function
        except FileNotFoundError:
            print(f"File not found: {file}")
        except Exception as e:
            print(f"Unexpected error with file {file}: {e}")

if __name__ == "__main__":
    main()