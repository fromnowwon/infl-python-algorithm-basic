import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
g = [[0] * (n+1) for _ in range(n+1)]

