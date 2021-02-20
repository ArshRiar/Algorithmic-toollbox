def Fibonacci_Number(n):
    n=n%60
    if n<=1:
        k=n
    else:
        i=0
        j=1
        for num in range(n-1):
            k=(i+j)%10
            i=j
            j=k
    return k
n=int(input())
print( Fibonacci_Number(n)*Fibonacci_Number(n+1)%10)