"""
The New Year: Meeting Friends

https://codeforces.com/problemset/problem/723/A
"""

def main():
    coordinates = list(map(int, input().split(" ")))
    coordinates.sort()
    min_total_distance = (coordinates[1] - coordinates[0]) + (coordinates[2] - coordinates[1])
    print(min_total_distance)


if __name__=="__main__":
    main()
