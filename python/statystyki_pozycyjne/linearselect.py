def linearselect(A,k):

    def find_median(A,p,r):
   
        while p<r:
            n = (r-p+1 + 4) // 5
        
            for i in range(p,r  + 1,5):
                insertion_sort(A,i,i+4)
            
            #C = [0]*n
            for i in range(n - 1):
                A[p+i],A[p+i*5 + 2] = A[p+i*5 + 2],A[p+i]
            tmp  = ((r-p+1)  - (n-1)*5)//2
            A[p+n - 1] , A[p+(n-1)*5 + tmp] = A[p+(n-1)*5 + tmp] , A[p+n-1]
            
            r=p+n-1
            
        return A[p]


    def select(A,p,r,k):
    
        pivot = find_median(A,p,r)
        q = partition(A,p,r,pivot)

        if q == k:
            return A[q]
        elif q > k:
            return select(A,p,q-1,k)
        else:
            return select(A,q+1,r,k)


    def insertion_sort(tab,p,r):
        if r >= len(tab):
            r = len(tab) - 1
        
        for i in range(p+1,r+1):
            val = tab[i]
            j = i - 1 
            while val < tab[j] and j >= p:
                tab[j+1] = tab[j]
                j-=1
            tab[j+1] = val
        
        return tab

    def partition(T,p,r,pivot):
    
        a = p
        b = p - 1
        T[p],T[r] = T[r],T[p]
        for a in range(p,r):
             
            if T[a] <= pivot:
                b+=1
                T[a] , T[b] = T[b] , T[a]
        T[b+1],T[r] = T[r],T[b+1]
    
        return b+1

    return select(A,0,len(A)-1,k)







from random import randint
from time import time
size = randint(10000,100000)
A = [randint(1,size) for i in range(size)]

k = len(A)* 5 // 10

start = time()
print("linear: " ,linearselect(A,k))
end = time()
result = end -start
print("czas: {0:02f}s".format(result))


