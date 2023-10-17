import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def DFS(L):


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)