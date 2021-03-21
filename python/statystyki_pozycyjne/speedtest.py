from random import randint
from time import time

def select(A,p,r,k):
    if p == r:
        return A[p]
    
    q = partition2(A,p,r)
    if q == k:
        return A[q]
    elif q > k:
        return select(A,p,q-1,k)
    else:
        return select(A,q+1,r,k)



def partition2(A,p,r):
  
    a = p
    b = p - 1
    x = A[r]
    for a in range(p,r):
        if A[a] <= x:
            b+=1
            A[a] , A[b] = A[b] , A[a]
    A[b+1],A[r] = A[r],A[b+1]
   
    return b+1


def find_median2(A):
   
    while len(A) > 1:
        n = (len(A)+ 4) // 5
        #B = [0]* n
        #j = 0
        for i in range(0,len(A),5):
          
            insertion_sort2(A,i,i+4)
            #j+=1
   
        C = [0]*n
        for i in range(n - 1):
            C[i] = A[i*5 + 2]
        tmp  = (len(A)  - (n-1)*5)//2
        C[n - 1] = A[(n-1)*5 + tmp]
        A = C
        

    return A[0]



def linearsort2(A,p,r,k):
  
    B = A[p:r+1]
   
    pivot = find_median2(B)
    #print("pivot: ",pivot)
   

    q = partition(A,p,r,pivot)
    #print("indeks pivota: ",q)
   
    #print("tablica: ",A)
    if q == k:
        return A[q]
    elif q > k:
        return linearsort2(A,p,q-1,k)
    else:
        return linearsort2(A,q+1,r,k)


def insertion_sort2(tab,p,r):
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




from math import ceil

def find_median(A):
   
    while len(A) > 1:
        n =(len(A)+4) // 5 
        B = [0]* n
        j = 0
        for i in range(0,len(A),5):
            B[j] = A[i:i+5]
            insertion_sort(B[j])
            j+=1
   
        C = [0]*n
        for i in range(n):
            C[i] = B[i][len(B[i])//2]

        A = C

    return A[0]



def linearsort(A,p,r,k):
  
    B = A[p:r+1]
   
    pivot = find_median(B)
    #print("pivot: ",pivot)
   

    q = partition(A,p,r,pivot)
    #print("indeks pivota: ",q)
   
    #print("tablica: ",A)
    if q == k:
        return A[q]
    elif q > k:
        return linearsort(A,p,q-1,k)
    else:
        return linearsort(A,q+1,r,k)


def insertion_sort(tab):
    n = len(tab)
    for i in range(1,n):
        val = tab[i]
        j = i - 1 
        while val < tab[j] and j >= 0:
            tab[j+1] = tab[j]
            j-=1
        tab[j+1] = val
    
    return tab











def linearsort3(A,k):

    def find_median3(A,p,r):
   
        while p<r:
            n = (r-p+1 + 4) // 5
        
            for i in range(p,r  + 1,5):
                insertion_sort3(A,i,i+4)
            
            #C = [0]*n
            for i in range(n - 1):
                A[p+i],A[p+i*5 + 2] = A[p+i*5 + 2],A[p+i]
            tmp  = ((r-p+1)  - (n-1)*5)//2
            A[p+n - 1] , A[p+(n-1)*5 + tmp] = A[p+(n-1)*5 + tmp] , A[p+n-1]
            
            r=p+n-1
            
        return A[p]


    def sort3(A,p,r,k):
    
       
    
        pivot = find_median3(A,p,r)
    
        q = partition3(A,p,r,pivot)
    

        if q == k:
            return A[q]
        elif q > k:
            return sort3(A,p,q-1,k)
        else:
            return sort3(A,q+1,r,k)


    def insertion_sort3(tab,p,r):
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

    def partition3(T,p,r,pivot):
    
        a = p
        b = p - 1
        T[p],T[r] = T[r],T[p]
        for a in range(p,r):
            
                
            if T[a] <= pivot:
                b+=1
                T[a] , T[b] = T[b] , T[a]
        T[b+1],T[r] = T[r],T[b+1]
    
        return b+1

    return sort3(A,0,len(A)-1,k)






size = randint(10000,100000)
A1 = [randint(1,size) for i in range(size)]

A2 = sorted(A1[0:])
A3 = A1[0:]
k = len(A1)* 5 // 10
#start = time()
#print("mag 1: " ,linearsort(A1,0,len(A1)-1,k))
#end = time()
#result = end -start
#print("czas: {0:02f}s".format(result))
#print("")
print("rozmiar tab: ",size)
start = time()
print("mag 2: " ,linearsort2(A1,0,len(A1)-1,k))
end = time()
result = end -start
print("czas: {0:02f}s".format(result))


start = time()
print("mag 3: " ,linearsort3(A2,k))
end = time()
result = end -start
print("czas: {0:02f}s".format(result))

start = time()
print("select: " ,select(A3,0,len(A3)-1,k))
end = time()
result = end -start
print("czas: {0:02f}s".format(result))

print("")



