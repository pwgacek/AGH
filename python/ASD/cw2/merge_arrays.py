from random import randint
def merge_arrays(T):

    n = len(T)

    if n > 1 :
        middle = n // 2
        lt = T[0: middle]
        rt = T[middle:n]

        return merge(T,merge_arrays(lt),merge_arrays(rt))

    else:
        return T[0]


def merge(T,lt,rt):

    n = len(lt) + len(rt)
    T = [0 for k in range(n)]
    i=0
    j=0

    for k in range (n):

        if j == len(rt):
            T[k]=lt[i]
            i+=1
        elif i == len(lt):
            T[k]=rt[j]
            j+=1

        elif lt[i] <= rt[j]:
            T[k]=lt[i]
            i+=1
        else:
            T[k]=rt[j]
            j+=1
    
    return T

T = [[randint(1,20) for i in range(randint(1,5))] for i in range(5)]
for i in range(5):
    T[i] = sorted(T[i])
print(T)

print(merge_arrays(T))