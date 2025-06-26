#!/usr/bin/env python3
from checkmate import is_king_attacked
import textwrap

def main():
    board_input = textwrap.dedent("""
        ....
        .K..
        ..P.
        ....
    """)
    is_king_attacked(board_input)

if __name__ == "__main__":
    main()

