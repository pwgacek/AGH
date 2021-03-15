from random import randint
def mergesort(T):
    while True:
        inwersja = []
        for i in range(len(T)-1):
            if T[i+1]<T[i]:
                inwersja.append(i)
        inwersja.append(len(T)-1)
        if len(inwersja)==1:
            return T
        p=0
        while len(inwersja)>1:
            merge(T, p, inwersja[0], inwersja[1])
            p = inwersja[1]+1
            inwersja = inwersja[2:]

def merge(T, p,q,r):
    A=T[p:q+1]
    B=T[q+1:r+1]
    i=p
    while len(A)>0 and len(B)>0:
        if A[0]<B[0]:
            T[i]=A.pop(0)
        else:
            T[i]=B.pop(0)
        i+=1
    while len(A)>0:
        T[i]=A.pop(0)
        i+=1
    while len(B)>0:
        T[i]=B.pop(0)
        i+=1
    return T

T = [[] for i in range(10)]
for i in range(10):
    T[i] = [randint(1,15) for i in range(randint(1,5))]

for i in range(len(T)):
    T[i] = sorted(T[i])
    tab=[]
for i in range(len(T)):
    for j in range(len(T[i])):
        tab.append(T[i][j])
print(tab)
print(mergesort(tab))
