import sys
sys.stdin = open("input.txt", "rt")
a = list(range(21)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for _ in range(10): # 10개의 구간
    s, e = map(int, input().split())
    for i in range((e - s + 1) // 2):
        a[s + i], a[e - i] = a[e - i], a[s + i] # swap

a.pop(0) # 0번째 인덱스 요소 없애기

for x in a:
    print(x, end=' ')