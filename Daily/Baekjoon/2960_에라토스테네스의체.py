import sys, math
input = sys.stdin.readline

#소수확인 함수
def prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))):
        if n%i == 0:
            return False
    return True

n,k = map(int,input().rstrip().split())
check = [0 for _ in range(n+1)]

#삭제실행
for i in range(2,n+1):
    if prime(i):
        for j in range(i, n+1, i):
            if check[j]==0:
                check[j]=1
                k-=1
                if k==0:
                    result = j
                    break

print(result)
