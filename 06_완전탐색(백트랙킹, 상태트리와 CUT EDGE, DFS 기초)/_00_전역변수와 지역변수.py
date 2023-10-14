def DFS():
    # a[0] = 7
    # print(a) # [1, 2, 3]
    a = [7, 8]
    print(a)

def DFS1():
    cnt = 3 # 지역 변수
    print(cnt)

def DFS2():
    if cnt == 5:
        print(cnt)

if __name__ == "__main__":
    cnt = 5
    a = [1, 2, 3]
    DFS()
    print(a)
    DFS1()
    DFS2()
    print(cnt)