"""
Helpful Maths

https://codeforces.com/problemset/problem/339/A
"""

def main():
    unordered_sum = input()
    numbers = unordered_sum.split("+")
    numbers.sort()
    ordered_sum = "+".join(numbers)
    print(ordered_sum)


if __name__=="__main__":
    main()
