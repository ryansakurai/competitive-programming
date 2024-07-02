"""
Buy a Shovel

https://codeforces.com/contest/732/problem/A
"""

# SHOVEL_PRICE * qt_shovels = 10*qt_coins + SINGLE_COIN_VALUE?

def main():
    shovel_price, single_coin_value = map(int, input().split(" "))

    qt_shovels = 1
    while True:
        if qt_shovels*shovel_price % 10 == 0:
            break
        if (qt_shovels*shovel_price - single_coin_value) % 10 == 0:
            break
        qt_shovels += 1

    print(qt_shovels)


if __name__=="__main__":
    main()
