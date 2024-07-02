"""
Little Nikita

https://codeforces.com/contest/1977/problem/A
"""

def main():
    qt_cases = int(input())
    results = []

    for _ in range(qt_cases):
        qt_moves, final_qt_cubes = map(int, input().split(" "))
        if qt_moves >= final_qt_cubes and (qt_moves - final_qt_cubes) % 2 == 0:
            results.append("Yes")
        else:
            results.append("No")

    for result in results:
        print(result)


if __name__=="__main__":
    main()
