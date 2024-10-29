"""
Prefiquence

https://codeforces.com/problemset/problem/1968/B
"""

def main():
    qt_cases = int(input())
    results = []

    for _ in range(qt_cases):
        _ = input()
        potential_subsequence = input()
        whole_string = input()

        current_idx = 0
        for char in whole_string:
            if current_idx >= len(potential_subsequence):
                break
            if char == potential_subsequence[current_idx]:
                current_idx += 1

        results.append(current_idx)

    for result in results:
        print(result)


if __name__=="__main__":
    main()
