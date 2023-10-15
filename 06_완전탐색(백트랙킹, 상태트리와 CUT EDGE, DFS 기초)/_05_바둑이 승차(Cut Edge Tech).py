import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

if __name__ == "__main__":
    c, n = map(int, input().split())
    a = [0] * n
    result = -2147000000
    for i in range(n):
        a[i] = int(input())
