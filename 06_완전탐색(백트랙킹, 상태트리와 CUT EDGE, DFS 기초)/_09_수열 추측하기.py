import sys
sys.stdin = open("input.txt", "r")
#def DFS(L, sum):

if __name__ == "__main__":
    n, f = map(int, input().split())
    p = [0] * n
    b = [1] * n
    ch = [0] * (n + 1)

    for i in range(1, n):
        b[i] = b[i - 1] * (n - 1) // i

    for x in b:
        print(x, end=' ')