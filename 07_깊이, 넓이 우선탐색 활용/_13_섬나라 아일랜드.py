import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n = int(input())
board = [list(map(int(input().split()))) for _ in range(n)]
cnt = 0
Q = deque()

