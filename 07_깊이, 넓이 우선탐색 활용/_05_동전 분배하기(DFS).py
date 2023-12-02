import sys
sys.stdin = open("input.txt", "rt")

if __name__ == "__main__":
    n = int(input())
    coin = []
    money = [0] * 3
    res = 2147000000

    for _ in range(n):
        coin.append(int(input()))
