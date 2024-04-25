"""
Maximise The Score

https://codeforces.com/problemset/problem/1930/A
"""

def main():
    qt_cases = int(input())

    results = []
    for _ in range(qt_cases):
        n = int(input())

        numbers = list(map(int, input().split(" ")))
        numbers.sort()

        sum_numbers = 0
        for _ in range(n):
            sum_numbers += numbers[-2]
            numbers.pop()
            numbers.pop()
        results.append(sum_numbers)

    for item in results:
        print(item)


if __name__=="__main__":
    main()
