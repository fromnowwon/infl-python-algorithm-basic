import sys
import itertools as it
sys.stdin = open("input.txt", "rt")
n, f = map(int, input().split())
b = [1] * n
cnt = 0

for i in range(1, n):
    b[i] = b[i - 1] * (n - i) / i
a = list(range(1, n + 1))

for tmp in it.permutations(a, 3):
    sum = 0
    for L, x in enumerate(tmp):
        sum += (x * b[L])