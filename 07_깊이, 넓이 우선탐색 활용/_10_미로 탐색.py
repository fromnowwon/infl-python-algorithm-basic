import sys
sys.stdin = open("input.txt", "rt")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt

if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    board[0][0] = 1
    DFS(0, 0)
    print(cnt)