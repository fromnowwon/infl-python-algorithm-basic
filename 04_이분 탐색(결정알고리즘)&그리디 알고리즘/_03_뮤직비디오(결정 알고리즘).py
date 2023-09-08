import sys
sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
Music = list(map(int, input().split()))
lt = 1
rt = sum(Music)
res = 0