import sys
sys.stdin = open("input.txt", "rt")
def DFS(L):


if __name__=="__main__":
    n, m = map(int, input().split())
    res = [0] * n
    ch = [0] * (n + 1)
    cnt = 0
    DFS(0)