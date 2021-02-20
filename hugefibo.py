def get_pasino_period(m):
    a=0
    b=1
    for i in range(m*m):
        c=(a+b)%m
        a=b
        b=c 
        if a==0 and b==1:
            return i+1
def get_huge_fibo(n,m):
    n=n%get_pasino_period(m)
    a=0
    b=1
    if n<=1:
        return n
    for i in range(n-1):
        c=(a+b)%m
        a=b 
        b=c 
    return c
n,m=map(int,input().split())
print(get_huge_fibo(n,m))