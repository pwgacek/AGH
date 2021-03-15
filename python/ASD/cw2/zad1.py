from random import randint

class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
import time
def merge(z1, z2):
    if z1 == None:
        return z2
    if z2 == None:
        return z1
    
    if z1.value < z2.value:
        result = z1
        result.next = merge(z1.next, z2)
    else:
        result = z2
        result.next = merge(z1, z2.next)
    
    return result

def split(L):
    N=L
    print("wrucam do splita:")
    printall(N)
    head2 = None
    if not N :
        print("dostalem pusty")
        return None,None
    while N.next:
    
        if N.value<=N.next.value:
      
            N=N.next
            
        else:
          
            head2=N.next
            N.next=None
       
    print("posplit:")    
    printall(L)
    printall(head2)
    print("--------")
    return L,head2
def merge_sort(L):
    
    is_sorted=False
    while not is_sorted:
        sorted=None
        is_sorted=True
       
        print("od nowa")
        while L:
            print("L wynosi: ")
            printall(L)
            print("lewy")
            left,L=split(L)
            print("prawy")
            right,L=split(L)
            #left right może być puste, ale nasz merge zadziała dobrze 
            if right:
                print("xd")
           
                is_sorted=False
            x=merge(left,right)
            
            print("pomerge")
            printall(x)
            i=x
            while i.next:
                i=i.next
            i.next=sorted
            sorted=x
            print("sorted wynosi: ")
            printall(sorted)
        L=sorted
    
    return sorted


def insert(start, n):
    q = Node(n)

    p = start
    prev = None

    while p != None:
        prev = p
        p = p.next

    if prev == None:
        return q

    prev.next = q
    return start


def printall(start):
    while start != None:
        print(start.value,end=" ")
        start = start.next
    print("")

z1 = insert(None,2)
z1 = insert(z1,3)
z1 = insert(z1,3)
z1 = insert(z1,4)
z1 = insert(z1,3)
z1 = insert(z1,5)
z1 = insert(z1,7)
z1 = insert(z1,3)
T = [[] for i in range(10)]
for i in range(10):
    T[i] = [randint(1,15) for i in range(randint(1,5))]
print(T)
for i in range(len(T)):
    T[i] = sorted(T[i])
z1=insert(None,1)
for i in range(len(T)):
    for j in range(len(T[i])):
        z1 = insert(z1,T[i][j])

printall(z1)
z1 = merge_sort(z1)
printall(z1)