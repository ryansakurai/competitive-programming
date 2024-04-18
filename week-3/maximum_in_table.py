"""
Maximum in Table

https://codeforces.com/problemset/problem/509/A
"""

def main():
    dimension = int(input())
    matrix = [[None]*dimension for _ in range(dimension)]
    for i in range(dimension):
        for j in range(dimension):
            if i == 0 or j == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    print(matrix[dimension-1][dimension-1])


if __name__=="__main__":
    main()
