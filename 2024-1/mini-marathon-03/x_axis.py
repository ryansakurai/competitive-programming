"""
X Axis

https://codeforces.com/contest/1986/problem/A
"""

def main():
    qt_cases = int(input())
    results = []

    for _ in range(qt_cases):
        x = list(map(int, input().split(" ")))

        x.sort()
        total_dist = abs(x[0] - x[1]) + abs(x[1] - x[2])

        results.append(total_dist)

    for result in results:
        print(result)


if __name__=="__main__":
    main()
