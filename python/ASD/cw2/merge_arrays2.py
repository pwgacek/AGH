from random import randint
def buildheap(A):
    n = len(A)
    def parent(i):return (i-1)//2 
    
    for i in range(parent(n-1),-1,-1):
        heapify(A,n,i)


def heapify(A,n,i):
    l = 2*i + 1
    r = l + 1
    m = i
    if l < n and A[l] < A[m] : m = l
    if r < n and A[r] < A[m] : m = r
    if m != i :
        A[i],A[m] = A[m],A[i]
        heapify(A,n,m)

def merge(T,n):
    A = []
    k = len(T)
    for i in range(len(T)):
       
        A.append(T[i][0])
        T[i].pop(0)
    
    buildheap(A) #klogk
    B = []
    i = 0
    while i < n - k:
        for j in range(k):
            if T[j] != []:
                i+=1
                B.append(A[0])
                print("przed")
                print(A)
                A[0] = T[j][0]
                print("dodaje: ", A[0])
                print("po")
                heapify(A,k,0)
                print(A)
                T[j].pop(0)

    for z in range(k-1,-1,-1):
        B.append(A[0])
        A[0],A[z] = A[z],A[0]
        heapify(A,z,0)

    return B



T = [[12, 16, 20], [3, 3, 20], [9, 16], [9, 12], [5, 8, 17, 19, 20]]

n = 0
for i in range(5):
    n+=len(T[i])
    T[i] = sorted(T[i])
print(T)

print(merge(T,n))
    