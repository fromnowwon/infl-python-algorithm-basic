import sys
sys.stdin = open("input.txt", "rt")


if __name__ == "__main__":
    n, m = map(int, input().split())
    pv = list()
    pt = list()

    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)

    res = -2147000000