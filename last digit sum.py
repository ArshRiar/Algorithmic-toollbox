def Fibonacci_Number_last_digit(n):
    if n<=1 or (n>=60 and n%60==1) or (n>=60 and n%60==0) :
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
n=int(input())
print( Fibonacci_Number_last_digit(n))