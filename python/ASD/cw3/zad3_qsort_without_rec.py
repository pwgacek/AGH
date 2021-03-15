from random import randint
def quick_sort(T,l,p):
  n = len(T)

  stos = []
  stos.append((0,n-1))

  while len(stos)>0:
    l,p=stos.pop()

    i = l
    j = p

    x = T[(l+p)//2]
    while i<=j:
      while T[i] < x:
        i+=1
      while T[j]>x:
        j-=1
      if i<=j:
        T[j],T[i]=T[i],T[j]
        i+=1
        j-=1
    if l < j:
      stos.append((l,j))
    if i<p:
      stos.append((i,p))

def quick_sort2(T):
    n = len(T)
    p = 0
    r = n - 1

    stos = []
    stos.append((p,r))
    while len(stos) > 0:
        p,r = stos.pop()
        pivot = partition(T,p,r)
        if p < pivot - 1:
            stos.append((p,pivot-1))
        if pivot + 1 < r:
            stos.append((pivot+1,r))



def partition(T,p,r):
  
    a = p
    b = p - 1
    x = T[r]
    for a in range(p,r):
        if T[a] <= x:
            b+=1
            T[a] , T[b] = T[b] , T[a]
    T[b+1],T[r] = T[r],T[b+1]
   
    return b+1



T = [randint(1,20) for i in range(20)]
print(T)
T2 =T[0:]
quick_sort(T,0,len(T)-1)

print(T)
print("----")
print(T2)
quick_sort2(T2)
print(T2)