"""
Boy or Girl

https://codeforces.com/contest/236/problem/A
"""

def main():
    username = input()
    distinct_chars = set(username)
    if len(distinct_chars)%2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")


if __name__=="__main__":
    main()
