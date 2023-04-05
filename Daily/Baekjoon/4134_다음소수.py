import sys,math
input = sys.stdin.readline

def prime(n):
    if n<2: return False
    elif n==2 : return True
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i==0: return False
        return True

n = int(input())
for _ in range(n):
    num = int(input())
    while not prime(num): 
        num=num+1
    print(num)
