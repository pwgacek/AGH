#Pawel Gacek
def mergesort(T):
    n = len(T)

    if n > 1:
        middle = n // 2
        
        def merge(lt,rt):
            #scala dwie posortowane tablice
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

        