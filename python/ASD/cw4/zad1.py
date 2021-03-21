from random import randint
def radix_sort(A,d,base):
    n = len(A)
    T = [[0]*d]*n
    for i in range(n):
        T[i] = arr_conv(A[i],d,base)

    for p in range(d-1,-1,-1):
        T=counting_sort(T,d,p,base)

    for i in range(n):
        A[i] = num_conv(T[i],base)

    


def counting_sort(A,d,p,base):
    n = len(A)
    B = [0]*n
    for i in range(n):
        B[i] =[0]*d
    C = [0]*base
    for i in range(n):
        C[A[i][p]]+=1

    for i in range(1,base):
        C[i] +=C[i - 1]

    for i in range(n-1,-1,-1):
        B[C[A[i][p]] - 1 ]  = A[i]
        C[A[i][p]] -= 1
    return B    
def arr_conv(num,d,base):
    T = [0]*d
    for i in range(d-1,-1,-1):
        T[i] = num % base 
        num//=base
    return T

def num_conv(T,base):
    num = 0
    n = len(T)
    for i in range(n) :
        num = num + T[i]*(base**(n-i - 1)) 
    return num

n = 10    
A = [randint(0,n*n - 1) for i in range(n)]
print(A)

radix_sort(A,2,n)
print(A)
