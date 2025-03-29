"""
Presents

https://codeforces.com/contest/136/problem/A
"""

def main():
    _ = input()
    receivers_from_input = tuple(map(int, input().split()))
    receivers = tuple(receiver - 1 for receiver in receivers_from_input)
    gifters = [None] * len(receivers)

    for i, receiver in enumerate(receivers):
        gifters[receiver] = i

    gifters_for_output = tuple(str(gifter + 1) for gifter in gifters)
    print(" ".join(gifters_for_output))


if __name__=="__main__":
    main()
