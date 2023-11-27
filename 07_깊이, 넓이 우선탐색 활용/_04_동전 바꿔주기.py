import sys
sys.stdin = open("input.txt", "rt")

if __name__ == "__main__":
    n = int(input())
    G = list(map(int, input().split()))
    s = sum(G)
    res = set()
