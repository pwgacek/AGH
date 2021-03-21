from random import randint
def sort(T):
    n = len(T)
    A = []
    for i in range(n):
        if not binary_search(A,0,len(A)-1,T[i]):
            append_to_A(A,T[i])

 
  
    i = 0
    for j in range(len(A)):
        while A[j][1] > 0:
            T[i] = A[j][0]
            i+=1
            A[j][1]-=1
     

    return(T)
    
def binary_search(tab,l,r,val):
    middle = (r + l) // 2

    if l <= r:
        if tab[middle][0] == val:
            tab[middle][1]+=1
            return True
    
        elif tab[middle][0] > val:
            return binary_search(tab,l,middle-1,val)
        else:
            return binary_search(tab,middle+1,r,val)

    else: return False
 

def append_to_A(tab,num):
    tab.append([num,1])
    n = len(tab)
  
    val = tab[n-1]
    j = n - 2 
    while val[0] < tab[j][0] and j >= 0:
        tab[j+1] = tab[j]
        j-=1
    tab[j+1] = val
        

T = [randint(1,5) for i in range(100)]

print(sort(T)) 