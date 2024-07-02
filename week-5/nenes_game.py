"""
Nene's Game

https://codeforces.com/problemset/problem/1956/A
"""

def main():
    qt_cases = int(input())

    general_results = []
    for _ in range(qt_cases):
        _, _ = list(map(int, input().split(" ")))
        to_be_kicked_out = list(map(int, input().split(" ")))
        normalize_idxs(to_be_kicked_out)
        qts_players = list(map(int, input().split(" ")))

        test_case_results = []
        for qt_players in qts_players:
            qt_winners = play_game(to_be_kicked_out, qt_players)
            test_case_results.append(qt_winners)
        general_results.append(test_case_results)

    for test_case_results in general_results:
        output = " ".join(map(str, test_case_results))
        print(output)

def normalize_idxs(idxs: list[int]):
    for i, _ in enumerate(idxs):
        idxs[i] -= 1

def play_game(to_be_kicked_out: list[int], total_qt_players: int) -> int:
    current_qt_players = total_qt_players
    kicked_out = True

    while kicked_out:
        kicked_out = False
        for player in to_be_kicked_out:
            if player < current_qt_players:
                current_qt_players -= 1
                kicked_out = True

    return current_qt_players


if __name__=="__main__":
    main()
