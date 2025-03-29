"""
Vanya and Fence

https://codeforces.com/contest/677/problem/A
"""

def main():
    _, fence_height = map(int, input().split(" "))
    person_heights = map(int, input().split(" "))

    min_width = 0
    for height in person_heights:
        if height <= fence_height:
            min_width += 1
        else:
            min_width += 2

    print(min_width)

if __name__=="__main__":
    main()
