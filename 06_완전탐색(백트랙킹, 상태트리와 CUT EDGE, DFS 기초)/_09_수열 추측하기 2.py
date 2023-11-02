import sys
import itertools as it
sys.stdin = open("input.txt", "rt")
n, f = map(int, input().split())
b = [1] * n

for i in range(1, n):
    b[i] = b[i - 1] * (n - i) / i
a = list(range(1, n + 1))