from random import randint
class Heap():
    T1 = []
    T2 = []


    def heapify1(self,A,n,i):
        l = 2*i + 1
        r = l + 1
        m = i
        if l < n and A[l] < A[m] : m = l
        if r < n and A[r] < A[m] : m = r
        if m != i :
            A[i],A[m] = A[m],A[i]
            self.heapify1(A,n,m)


    def heapify2(self,A,n,i):
        l = 2*i + 1
        r = l + 1
        m = i
        if l < n and A[l] > A[m] : m = l
        if r < n and A[r] > A[m] : m = r
        if m != i :
            A[i],A[m] = A[m],A[i]
            self.heapify2(A,n,m)

    def goup1(self,A,i):
        
        def parent(i):return (i-1)//2 
        
       
        

        p = parent(i)
        while i != 0 and  A[p] > A[i]:
        
                A[p],A[i] = A[i] , A[p]
                i = p
                p = parent(i)
     
    def goup2(self,A,i):
        
        def parent(i):return (i-1)//2 
        
       
        

        p = parent(i)
        while i != 0 and  A[p] < A[i]:
            
                A[p],A[i] = A[i] , A[p]
                i = p
                p = parent(i)     

    def Insert(self, x):
       
        if len(self.T1) == 0:
            self.T1.append(x)

        else:

            if x > self.T1[0]:
                self.T1.append(x)
                self.goup1(self.T1,len(self.T1)-1)


            else:
                self.T2.append(x)
                self.goup2(self.T2,len(self.T2)-1)

     
        if (len(self.T1) - len(self.T2) ) > 1:
            self.T2.append(self.T1[0])
            self.goup2(self.T2,len(self.T2)-1)
            

            self.T1[0] = self.T1[len(self.T1)-1]
            self.T1.pop(len(self.T1) - 1)
            self.heapify1(self.T1,len(self.T1),0)

        elif len(self.T2) - len(self.T1) > 1:
            self.T1.append(self.T2[0])
            self.goup1(self.T1,len(self.T1)-1)

            self.T2[0] = self.T2[len(self.T2) - 1]
            self.T2.pop(len(self.T2) - 1)
            self.heapify2(self.T2,len(self.T2),0)

        print("self.T1: ",self.T1)
        print("self.T2: ",self.T2)
        print("---------")

    
    def GetMedian(self):
        if len(self.T1) == len(self.T2):
            return (self.T1[0] + self.T2[0]) /2
        elif len(self.T1) > len(self.T2):
            return self.T1[0]
        else:
            return self.T2[0]

z1 = Heap()

for i in range(10):
    z1.Insert(randint(1,20))
print(z1.GetMedian())