"""
Sushi for Two

https://codeforces.com/problemset/problem/1138/A
"""

class SushiType:
    TUNA = 1
    EEL = 2


def main():
    _ = input()
    sushis = list(map(int, input().split(" ")))

    largest_sequence = 0
    
    i=0
    while i < len(sushis):
        seq_first_half = count_sushis(sushis, i)
        i += seq_first_half
        seq_second_half = count_sushis(sushis, i)
        seq_whole = min(seq_first_half, seq_second_half)*2

        largest_sequence = seq_whole if seq_whole > largest_sequence else largest_sequence

    print(largest_sequence)

def count_sushis(sushis: list[SushiType], start_idx: int) -> int:
    if start_idx >= len(sushis):
        return 0

    type_to_count = sushis[start_idx]

    qt=0
    for i in range(start_idx, len(sushis)):
        if sushis[i] != type_to_count:
            break
        qt += 1

    return qt


if __name__=="__main__":
    main()
