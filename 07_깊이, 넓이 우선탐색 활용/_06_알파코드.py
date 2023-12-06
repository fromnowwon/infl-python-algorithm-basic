import sys
sys.stdin = open("input.txt", "rt")


if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1)
    res = [0] * (n + 3)
    cnt = 0
