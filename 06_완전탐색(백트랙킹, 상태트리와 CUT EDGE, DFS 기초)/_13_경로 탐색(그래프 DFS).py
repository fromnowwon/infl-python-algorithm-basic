import sys
sys.stdin = open("input.txt", "rt")


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n+1) for _ in range(n+1)]
    ch = [0] * (n+1)

    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
