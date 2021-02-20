def Fibonacci_Number(n):
    if n<=1:
        k=n
    else:
        i=0
        j=1
        for num in range(n-1):
            k=i+j
            i=j
            j=k
    return k
n=int(input())
print( Fibonacci_Number(n))