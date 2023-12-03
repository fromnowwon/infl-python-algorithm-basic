import sys
sys.stdin = open("input.txt", "rt")

def DFS(L):
    global res
    if L == n:

    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L+1)


if __name__ == "__main__":
    n = int(input())
    coin = []
    money = [0] * 3
    res = 2147000000

    for _ in range(n):
        coin.append(int(input()))

    DFS(0)