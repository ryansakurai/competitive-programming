"""
Even Array

https://codeforces.com/problemset/problem/1367/B
"""

from typing import Dict


class MismatchType:
    ITEM_NOT_EVEN = 0
    ITEM_NOT_ODD = 1


def main():
    qt_cases = int(input())
    results = []

    for _ in range(qt_cases):
        _ = input()
        array = list(map(int, input().split(" ")))
        qt_mismatches = count_mismatches(array)
        if qt_mismatches[MismatchType.ITEM_NOT_EVEN] == qt_mismatches[MismatchType.ITEM_NOT_ODD]:
            results.append(qt_mismatches[MismatchType.ITEM_NOT_EVEN])
        else:
            results.append(-1)

    for result in results:
        print(result)

def count_mismatches(array: list[int]) -> Dict[MismatchType, int]:
    qt_mismatches = {
        MismatchType.ITEM_NOT_EVEN: 0,
        MismatchType.ITEM_NOT_ODD: 0,
    }

    for idx, item in enumerate(array):
        if idx % 2 == 0 and item % 2 != 0:
            qt_mismatches[MismatchType.ITEM_NOT_ODD] += 1
        elif idx % 2 != 0 and item % 2 == 0:
            qt_mismatches[MismatchType.ITEM_NOT_EVEN] += 1

    return qt_mismatches


if __name__=="__main__":
    main()
