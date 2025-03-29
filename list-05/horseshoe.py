"""
Is your horseshoe on the other hoof?

https://codeforces.com/contest/228/problem/A
"""

def main():
    horseshoe_colors = list(input().split(" "))
    unique_colors = set(horseshoe_colors)
    print(4 - len(unique_colors))


if __name__=="__main__":
    main()
