"""
Bit++

https://codeforces.com/problemset/problem/282/A
"""

def main():
    qt_statements = int(input())

    x = 0
    for _ in range(qt_statements):
        statement = input()
        if "+" in statement:
            x += 1
        else:
            x -= 1
    print(x)


if __name__=="__main__":
    main()
