from random import randint
def merge(T):
  n = len(T)
  buildheap(T)

  B = []
  while T:
    B.append(T[0][0])
    T[0].pop(0)
    if not T[0]:
      T.pop(0)
      n = len(T)
      buildheap(T)

    heapify(T,n,0)


  return B  



def buildheap(T):
  n = len(T)
  for i in range(parent(n-1),-1,-1):
    heapify(T,n,i)



def heapify(T,n,i):
  l = left(i)
  r = right(i)
  m = i
  if l < n and T[l][0] < T[m][0] : 
    m = l
    
  if r < n and T[r][0] < T[m][0] :
    m = r
  if m != i:
    T[m],T[i] = T[i],T[m]
    heapify(T,n,m)
  


def parent(i):
  return (i-1)//2
def left(i):
  return 2*i + 1
def right(i):
  return 2*i +2


T = [[randint(1,20) for i in range(randint(1,5))] for i in range(5)]
for i in range(5):
    T[i] = sorted(T[i])
print(T)
T= merge(T)
print(T)
