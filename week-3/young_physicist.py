"""
Young Physicist

https://codeforces.com/contest/69/problem/A
"""

def main():
    qt_vectors = int(input())

    total_force = {"x": 0, "y": 0, "z": 0}
    for _ in range(qt_vectors):
        x, y, z = map(int, input().split(" "))
        total_force["x"] += x
        total_force["y"] += y
        total_force["z"] += z

    if total_force["x"] == total_force["y"] == total_force["z"] == 0:
        print("YES")
    else:
        print("NO")


if __name__=="__main__":
    main()
