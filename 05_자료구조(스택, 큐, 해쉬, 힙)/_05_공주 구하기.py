import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
dq = list(range(1, n+1))
dq = deque(dq)
