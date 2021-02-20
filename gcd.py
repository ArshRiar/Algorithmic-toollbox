def gcd(a,b):
    if b==0:
        return a 
    else:
        a=a%b
        return gcd(b,a)
a,b=map(int,input().split())
print(gcd(a,b))