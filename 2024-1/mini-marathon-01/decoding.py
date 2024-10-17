"""
Decoding

https://codeforces.com/contest/746/problem/B
"""

def main():
    _ = input()

    coded_word = input()

    decoded_letters = []
    for letter in coded_word[::-1]:
        decoded_letters.insert(len(decoded_letters) // 2, letter)

    decoded_word = "".join(decoded_letters)
    print(decoded_word)

if __name__ == "__main__":
    main()
