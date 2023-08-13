import sys
sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))
# ave = round(sum(a)/n) # 파이썬의 round는 round_half_even 방식을 택하기 때문에 0.5를 더하는 방식을 사용한다.
ave=sum(a)/n
ave=ave+0.5
ave=int(ave)
min = 2147000000

for idx, x in enumerate(a):
    tmp = abs(x - ave) # 절대값을 통해 평균과 학생의 점수의 차이를 구한다
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1 # 학생 번호
    elif tmp == min:
        if x > score: # 더 큰 점수의 학생으로 교체, 같은 점수가 여러 개여도 맨 앞 점수가 선택된다
            score = x
            res = idx + 1

print(ave, res)