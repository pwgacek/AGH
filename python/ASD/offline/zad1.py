from random import randint, seed





def mergesort(T):

    n = len(T)

    if n > 1:
        
        middle = n // 2
        
        def merge(lt,rt):
            
            n = len(lt) + len(rt)
            t_joined = [0 for k in range(n)]
            i=0
            j=0

            for k in range (n):

                if j == len(rt):
                    t_joined[k]=lt[i]
                    i+=1
                elif i == len(lt):
                    t_joined[k]=rt[j]
                    j+=1

                elif lt[i] <= rt[j]:
                    t_joined[k]=lt[i]
                    i+=1
                else:
                    t_joined[k]=rt[j]
                    j+=1
    
            return t_joined


        return  merge(mergesort(T[0:middle]),mergesort(T[middle:n]))

    
    else : return T
  
  
  
  

seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]

print("przed sortowaniem: T =", T) 
T = mergesort(T)
print("po sortowaniu    : T =", T)
print(T)
for i in range(len(T)-1):
  if T[i] > T[i+1]:
    print("Błąd sortowania!")
    exit()
    
print("OK")