"""
Problem Generator

https://codeforces.com/contest/1980/problem/A
"""

def main():
    qt_cases = int(input())
    results = []

    for _ in range(qt_cases):
        _, qt_rounds = map(int, input().split())
        problems = list(input())

        qt_problems = 0
        for letter in ("A", "B", "C", "D", "E", "F", "G"):
            new_problems = qt_rounds - problems.count(letter)
            if new_problems > 0:
                qt_problems += new_problems

        results.append(qt_problems)

    for result in results:
        print(result)


if __name__=="__main__":
    main()
