import sys
sys.stdin = open("input.txt", "rt")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt


if __name__ == "__main__":
    n = int(input())
    board = [[0] * n for _ in range(n)]
    ch = [[0] * n for _ in range(n)]
    max = -2147000000
    min = 2147000000

    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] < min:
                min = tmp[j]
                sx = i
                sy = j

            if tmp[j] > max:
                max = tmp[j]
                ex = i
                ey = j

            board[i][j] = tmp[j]

