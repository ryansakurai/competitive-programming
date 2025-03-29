"""
Balanced Round

https://codeforces.com/problemset/problem/1850/D
"""

def main():
    qt_cases = int(input())

    results = []
    for _ in range(qt_cases):
        _, max_diff = map(int, input().split(" "))
        difficulties = list(map(int, input().split(" ")))
        if len(difficulties) < 2:
            results.append(0)
            continue

        difficulties.sort()

        max_seq = 0
        current_seq = 1
        for i in range(1, len(difficulties)):
            if difficulties[i] - difficulties[i-1] <= max_diff:
                current_seq += 1
            else:
                current_seq = 1
            max_seq = current_seq if current_seq > max_seq else max_seq
        results.append(len(difficulties) - max_seq)

    for item in results:
        print(item)


if __name__=="__main__":
    main()
