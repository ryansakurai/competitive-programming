"""
Twins

https://codeforces.com/problemset/problem/160/A
"""

def main():
    _ = input()
    coins = list(map(int, input().split()))

    his_coins = coins
    my_coins = []

    his_coins.sort()
    while sum(his_coins) >= sum(my_coins):
        coin_taken = his_coins.pop()
        my_coins.append(coin_taken)

    print(len(my_coins))


if __name__=="__main__":
    main()
