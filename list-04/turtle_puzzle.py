"""
Turtle Puzzle: Rearrange and Negate

https://codeforces.com/problemset/problem/1933/A
"""

def main():
    qt_cases = int(input())

    results = []
    for _ in range(qt_cases):
        _ = input()

        numbers = list(map(int, input().split(" ")))
        numbers.sort()

        for i, number in enumerate(numbers):
            if number >= 0:
                break
            numbers[i] = -number

        results.append(sum(numbers))

    for item in results:
        print(item)


if __name__=="__main__":
    main()
