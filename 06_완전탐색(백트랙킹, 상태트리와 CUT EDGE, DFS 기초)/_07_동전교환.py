import sys
sys.stdin = open("input.txt", "r")
def DFS(L, sum):

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    res = 2147000000
    a.sort(reverse=True)
    DFS(0, 0)