import sys
sys.stdin = open("input.txt", "rt")

def DFS(L, s, sum):


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)