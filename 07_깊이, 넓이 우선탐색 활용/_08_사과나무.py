import sys
sys.stdin = open("input.txt", "rt")
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
sum = 0
Q = deque()

ch[n//2][n//2]
Q.append((n//2, n//2))
L = 0

while True:
    if L==n//2:
        break