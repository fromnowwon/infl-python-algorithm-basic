import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
seq = [0] * n