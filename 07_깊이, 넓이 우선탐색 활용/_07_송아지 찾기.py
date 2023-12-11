import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

MAX = 100000
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
n, m = map(int, input().split())
