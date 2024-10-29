"""
Target Practice

https://codeforces.com/contest/1873/problem/C
"""

class Target:
    def __init__(self):
        self.__QUARTER_TARGET = [
            [1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2],
            [1, 2, 3, 3, 3],
            [1, 2, 3, 4, 4],
            [1, 2, 3, 4, 5],
        ]
        self.score = 0

    def hit(self, x: int,  y: int) -> int:
        if x < len(self.__QUARTER_TARGET):
            internal_x = x
        else:
            internal_x = len(self.__QUARTER_TARGET)*2 - (x+1)
        
        if y < len(self.__QUARTER_TARGET[0]):
            internal_y = y
        else:
            internal_y = len(self.__QUARTER_TARGET[0])*2 - (y+1)

        self.score += self.__QUARTER_TARGET[internal_x][internal_y]
        return self.__QUARTER_TARGET[internal_x][internal_y]


def main():
    qt_cases = int(input())
    results = []

    for _ in range(qt_cases):
        target = Target()

        for x in range(10):
            line = input()
            for y, cell in enumerate(line):
                if cell == "X":
                    target.hit(x, y)

        results.append(target.score)

    for result in results:
        print(result)


if __name__=="__main__":
    main()
