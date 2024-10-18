"""
Summer sell-off

https://codeforces.com/contest/810/problem/B
"""

def main():
    qt_days_total, qt_days_to_choose = map(int, input().split())

    days = []
    for _ in range(qt_days_total):
        qt_products, qt_clients = map(int, input().split())
        days.append({
            "qt_products": qt_products,
            "qt_clients": qt_clients,
        })

    days.sort(
        key=lambda day: min(day["qt_products"]*2, day["qt_clients"]) - min(day["qt_products"], day["qt_clients"]),
        reverse=True,
    )

    products_sold = 0
    for day in days:
        if qt_days_to_choose > 0:
            day["qt_products"] *= 2
            qt_days_to_choose -= 1
        products_sold += min(day["qt_products"], day["qt_clients"])

    print(products_sold)


if __name__=="__main__":
    main()
