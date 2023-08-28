import sys
sys.stdin = open("input.txt", "r")
# sort()를 사용하면 nlogn
# n번 만에 해결하는 방법으로 해결하자

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
p1 = p2 = 0
c = []

while p1 < n and p2 < n:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

if p1 < n:
    c = c + a[p1:]

if p2 < n:
    c = c + b[p2:]

for x in c:
    print(x, end=' ')