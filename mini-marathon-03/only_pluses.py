"""
Only Pluses

https://codeforces.com/contest/1992/problem/A
"""

def main():
    qt_cases = int(input())
    results = []

    for _ in range(qt_cases):
        integers = list(map(int, input().split(" ")))

        for _ in range(5):
            if integers[0] <= integers[1] and integers[0] <= integers[2]:
                integers[0] += 1
            elif integers[1] <= integers[0] and integers[1] <= integers[2]:
                integers[1] += 1
            else:
                integers[2] += 1

        results.append(integers[0]*integers[1]*integers[2])

    for result in results:
        print(result)


if __name__=="__main__":
    main()
