def insert_to_heap(A,num):
    
    A.append([num,1])
    i = len(A) - 1

    while i != 0 and  A[parent(i)][0] < A[i][0]:
      
            A[parent(i)],A[i] = A[i] , A[parent(i)]
            i = parent(i)

def parent(i):
  return (i-1)//2
def left(i):
  return 2*i + 1
def right(i):
  return 2*i +2

def find_in_heap(A,num,i=0):
    while i < len(A) and A[i][0] >= num:
       
        if A[i][0] == num:
            A[i][1]+=1
            return True
            
        if find_in_heap(A,num,left(i)) : return True

        i = right(i)

    return False

def quick_sort(T,p,r):

    while p < r :
        pivot = partition(T,p,r)

        if (pivot - p) < (r - pivot):
            quick_sort(T,p,pivot-1)
            p = pivot + 1
        else:
            quick_sort(T,pivot+1,r)
            r = pivot - 1
        
   


def partition(T,p,r):
  
    a = p
    b = p - 1
    x = T[r][0]
    for a in range(p,r):
        if T[a][0] <= x:
            b+=1
            T[a] , T[b] = T[b] , T[a]
    T[b+1],T[r] = T[r],T[b+1]
   
    return b+1


      
def sort(T):
    n = len(T)    
    A = []
    for i in range(n):
        if not find_in_heap(A,T[i]):
            print("dodaje: ",T[i])
            insert_to_heap(A,T[i])
    
    quick_sort(A,0,len(A)-1)
    j = 0
    for i in range(len(A)):
        while A[i][1] > 0:
            T[j] = A[i][0]
            j+=1
            A[i][1]-=1
    return(T)
#####

from random import randint
T = [randint(1,10) for i in range(20)]
print(T)
print(sort(T))



