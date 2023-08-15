import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
ch = [0] * (n+1) # 인덱스 번호가 n까지 있어야 하니까 1을 더한다. 반복문 돌 때에는 인덱스 1~n+1까지 돌면 된다.
cnt = 0

for i in range(2, n+1): # 1은 무조건 소수이기 때문에 인덱스 2부터 n까지 돈다
    if ch[i] == 0:
        cnt += 1
        # i의 배수 찾기.이미 i에서 체크되므로 i의 배수는 소수에서 제외
        for j in range(i, n+1, i): # 3번째 인자는 얼만큼의 간격으로 순환할지를 정함
            ch[j] = 1

print(cnt)
