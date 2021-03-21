from math import ceil
from random import randint

def linearselect(A,k):

    def find_median(A,p,r):
   
        while p<r:
            n = (r-p+1 + 4) // 5
        
            for i in range(0,r - p + 1,5):
                insertion_sort(A,i,i+4)
            
            #C = [0]*n
            for i in range(n - 1):
                A[i],A[i*5 + 2] = A[i*5 + 2],A[i]
            tmp  = ((r-p+1)  - (n-1)*5)//2
            A[n - 1],A[(n-1)*5 + tmp] = A[(n-1)*5 + tmp],A[n-1]
            p=0
            r=n-1
            
        return A[0]


    def sort(A,p,r,k):
    
        B = A[p:r+1]
    
        pivot = find_median(B,0,len(B)-1)
    
        q = partition(A,p,r,pivot)
    

        if q == k:
            return A[q]
        elif q > k:
            return sort(A,p,q-1,k)
        else:
            return sort(A,q+1,r,k)


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
        for a in range(p,r):
            if T[a] == pivot : 
                T[a],T[r] = T[r],T[a]
            if T[a] <= pivot:
                b+=1
                T[a] , T[b] = T[b] , T[a]
        T[b+1],T[r] = T[r],T[b+1]
    
        return b+1

    return sort(A,0,len(A)-1,k)





A = [randint(1,1000) for i in range(100)]

k = len(A)//2
#print(A)
print(linearselect(A,k))

