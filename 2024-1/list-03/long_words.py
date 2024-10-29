"""
Way Too Long Words

https://codeforces.com/problemset/problem/71/A
"""

def main():
    qt_words = int(input())

    result = []
    for _ in range(qt_words):
        word = input()
        if len(word) <= 10:
            result.append(word)
        else:
            abbreviation = word[0] + str(len(word)-2) + word[-1]
            result.append(abbreviation)

    for word in result:
        print(word)


if __name__=="__main__":
    main()
