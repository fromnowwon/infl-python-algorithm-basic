import sys
sys.stdin = open("input.txt", "r")

n = int(input())
meeting = []

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

# 끝나는 시간을 기준으로 정렬한다.
meeting.sort(key=lambda x : (x[1], x[0])) # x: (1순위, 2순위)

et = 0
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1

print(cnt)