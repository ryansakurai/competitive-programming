"""
Football

https://codeforces.com/problemset/problem/96/A
"""

def main():
    players = input()

    dangerous = False
    sequence = 1
    prev_player = None
    for i, _ in enumerate(players):
        if prev_player:
            if players[i] == players[i-1]:
                sequence += 1
            else:
                sequence = 1
        prev_player = players[i]

        if sequence >= 7:
            dangerous = True
            break

    print("YES" if dangerous else "NO")


if __name__=="__main__":
    main()
