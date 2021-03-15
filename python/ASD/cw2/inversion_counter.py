from random import randint
counter= 0


def inversion_counter(T):
    counter = 0
    _ , counter = merge_sort(T)
    return counter

def merge_sort(T):
    counter = 0
    n = len(T)
    if n > 1:
        middle = n // 2
        lt = T[0:middle]
        rt = T[middle:n]
        lt , x = merge_sort(lt)
        rt , y = merge_sort(rt)
        counter+=(x+y)
       
        return  merge(lt,rt,counter)
    else: return T, counter



def merge(lt,rt,counter):
    
    n = len(lt) + len(rt)
    T_joined = [0 for k in range(n)]
    i=0
    j=0

    for k in range (n):

        if j == len(rt):
            T_joined[k]=lt[i]
            i+=1
        elif i == len(lt):
            T_joined[k]=rt[j]
            j+=1

        elif lt[i] <= rt[j]:
            T_joined[k]=lt[i]
            i+=1
        else:
            T_joined[k]=rt[j]
            counter+=(len(lt) - i)
            j+=1
    
    return T_joined , counter


def test(T):
    licznik = 0
    n = len(T)
    for i in range(n-1):
        for j in range(i+1,n):
            if T[i] > T[j]: licznik += 1
    return licznik

    
T=[randint(1,1000) for i in range(10000)]

print(inversion_counter(T))
print(test(T))