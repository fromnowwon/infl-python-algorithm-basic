import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [list(map(int, input().split())) for _ in range(7)]
dis = [[0] * 7 for _ in range(7)]

Q = deque()
Q.append((0, 0))
board[0][0] = 1

while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]