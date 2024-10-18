"""
Team

https://codeforces.com/contest/231/problem/A
"""

def main():
    qt_problems = int(input())

    qt_to_implement = 0
    for _ in range(qt_problems):
        can_solve = input().split(" ").count("1")
        if can_solve >= 2:
            qt_to_implement += 1
    print(qt_to_implement)


if __name__=="__main__":
    main()
