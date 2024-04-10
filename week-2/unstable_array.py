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
    ## Max result is when you interpolate 0s with the positive numbers (ex. 0,2,0,3,0).
    ## You can devide the number equally between available spots and add the remainder to one of
    ## the numbers. This way, each number will be worth double its value in the result.
    ## When array_length is even, there will be a missing 0. Make sure it is the first or last one
    ## (we'll wanna choose the one whose neighbor is the least, because that number isn't gonna be double anymore).
    ## Since this number is gonna be worth less, pass this value onto the next positive number if there is one. This way,
    ## it will gain back its value.

    qt_positive = array_length // 2
    if qt_positive < 1:
        return 0

    least_number = array_sum // qt_positive
    remainder = array_sum % qt_positive
    output = qt_positive * least_number * 2
    output += remainder * 2

    if array_length%2 == 0 and array_length < 4:
        output -= least_number

    return output


if __name__=="__main__":
    main()
