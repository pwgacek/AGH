from random import randint
def select(A,p,r,k):
    if p == r:
        return A[p]
    
    q = partition(A,p,r)
    if q == k:
        return A[q]
    elif q > k:
        return select(A,p,q-1,k)
    else:
        return select(A,q+1,r,k)



def partition(A,p,r):
  
    a = p
    b = p - 1
    x = A[r]
    for a in range(p,r):
        if A[a] <= x:
            b+=1
            A[a] , A[b] = A[b] , A[a]
    A[b+1],A[r] = A[r],A[b+1]
   
    return b+1

A=[randint(1,10000000) for i in range(10000000)]
print(select(A,0,len(A)-1,5000000))