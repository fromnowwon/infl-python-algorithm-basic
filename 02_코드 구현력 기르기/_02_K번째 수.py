import sys
sys.stdin = open('input.txt', 'rt');
T = int(input()) # 첫번째 줄

for t in range (T): # 각 케이스 순환
    n, s, e, k = map(int, input().split()) # 두번째 줄
    a = list(map(int, input().split())) # 세번째 줄
    a = a[s-1:e] # s번째부터 e번째까지 추출
    a.sort() # 오름차순 정렬
    print("#%d %d" %(t+1, a[k-1])) # k번째 숫자 출력
