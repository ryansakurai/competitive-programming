"""
Angry Monk

https://codeforces.com/contest/1992/problem/B
"""

def main():
    qt_cases = int(input())
    results = []

    for _ in range(qt_cases):
        _, _ = map(int, input().split(" "))
        pieces = list(map(int, input().split(" ")))

        qt_op = 0
        pieces.sort()
        for i in range(len(pieces) - 1):
            qt_op += pieces[i]*2 - 1

        results.append(qt_op)

    for result in results:
        print(result)


if __name__=="__main__":
    main()
