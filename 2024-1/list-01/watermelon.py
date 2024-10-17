"""
Watermelon

https://codeforces.com/problemset/problem/4/A
"""

def main():
    SMALLEST_PIECE = 2
    total_weight = int(input())

    remaining_piece = total_weight - SMALLEST_PIECE
    if remaining_piece > 0 and remaining_piece%2 == 0:
        print("YES")
    else:
        print("NO")

if __name__=="__main__":
    main()
