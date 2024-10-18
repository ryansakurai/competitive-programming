"""
Most Unstable Array

https://codeforces.com/contest/1353/problem/A
"""

def main():
    qt_cases = int(input())
    results = []
    for _ in range(qt_cases):
        array_length, array_sum = map(int, input().split(" "))
        results.append(calc_max_sum_of_abs_diffs_between_adjacent_elements(array_length, array_sum))

    for result in results:
        print(result)

def calc_max_sum_of_abs_diffs_between_adjacent_elements(array_length: int, array_sum: int) -> int:
    ## Max result is when you surround the array_sum with 0s, that way it'll be worth double
    ## its value. If you can't have a 0s on both sides, its gonna be worth only its value.

    if array_length == 1:
        return 0
    if array_length == 2:
        return array_sum
    return array_sum * 2


if __name__=="__main__":
    main()
