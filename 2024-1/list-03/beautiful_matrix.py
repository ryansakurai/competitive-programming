"""
Beautiful Matrix

https://codeforces.com/contest/263/problem/A
"""

def main():
    GOAL_SPOT = {"x": 2, "y": 2}

    found = False
    for i in range(5):
        row = tuple(map(int, input().split(" ")))
        if not found and 1 in row:
            current_spot = {"x": i, "y": row.index(1)}
            found = True

    qt_moves = abs(GOAL_SPOT["x"] - current_spot["x"]) + abs(GOAL_SPOT["y"] - current_spot["y"])
    print(qt_moves)


if __name__=="__main__":
    main()
