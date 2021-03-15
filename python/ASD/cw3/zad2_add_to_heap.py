from random import randint
def insert_to_heap(A,i):
    
    A.append(i)
    i = len(T) - 1

    while i != 0 and  A[parent(i)] < A[i]:
      
            A[parent(i)],A[i] = A[i] , A[parent(i)]
            i = parent(i)
            
 
def parent(i):
    return (i-1)//2 


def buildheap(A):
    n = len(A)
    def parent(i):return (i-1)//2 
    
    for i in range(parent(n-1),-1,-1):
        heapify(A,n,i)

def heapify(A,n,i):
    l = 2*i + 1
    r = l + 1
    m = i
    if l < n and A[l] > A[m] : m = l
    if r < n and A[r] > A[m] : m = r
    if m != i :
        A[i],A[m] = A[m],A[i]
        heapify(A,n,m)


T = [randint(1,20) for i in range(20)]
print(T)
buildheap(T)
print(T)
liczba =randint(20,20)
print("liczba:", liczba)
insert_to_heap(T,liczba)

print(T)
