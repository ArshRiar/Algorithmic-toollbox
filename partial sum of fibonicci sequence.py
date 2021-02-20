def Fibonacci_Number_last_digit(n):
    if n<=0:
        return 0
    if n==1 or (n>=60 and n%60==1) or (n>=60 and n%60==0) :
        sum=n%60
    else:
        i=0
        j=1 
        sum=1 
        if n>60:
            n=n%60
        for t in range(n-1):
            k=i+j 
            sum=sum+k 
            i=j%10 
            j=k%10
    return sum%10    
n,m=map(int,input().split())
f=Fibonacci_Number_last_digit(m)-Fibonacci_Number_last_digit(n-1)
print(f%10)