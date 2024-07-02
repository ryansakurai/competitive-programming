"""
Domino piling

https://codeforces.com/problemset/problem/50/A
"""

def main():
    board_height, board_width = map(int, input().split(" "))
    print(board_height * board_width // 2)


if __name__=="__main__":
    main()
