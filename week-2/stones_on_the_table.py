"""
Stones on the Table

https://codeforces.com/contest/266/problem/A
"""

def main():
    _ = int(input())
    colors = list(input())

    count_repeated = 0
    prev_color = None
    for color in colors:
        if color == prev_color:
            count_repeated += 1
        prev_color = color
    print(count_repeated)


if __name__=="__main__":
    main()
