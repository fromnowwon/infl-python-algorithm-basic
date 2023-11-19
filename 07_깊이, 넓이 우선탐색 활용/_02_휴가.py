import sys
sys.stdin = open("input.txt", "rt")

def DFS(L, sum):
    global res


if __name__ == "__main__":
    n = int(input())
    T = list()
    P = list()

    for i in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)
    res = -2147000000
    T.insert(0, 0)
    P.insert(0, 0)
    DFS(1, 0)