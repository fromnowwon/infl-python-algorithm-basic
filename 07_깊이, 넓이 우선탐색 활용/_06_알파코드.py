import sys
sys.stdin = open("input.txt", "rt")

def DFS(L, P):
    global cnt
    if L == n:
        cnt += 1

    else:
        for i in range(1, 27):
            if code[L] == i:
                res[P] = i


if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1)
    res = [0] * (n + 3)
    cnt = 0
    DFS(0, 0)
    print(cnt)
