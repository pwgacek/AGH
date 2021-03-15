from random import randint
def ssp3(tab):
    n = len(tab)
    s_max = 0
    for i in range(n):
        for j in range(i,n):
            sum = 0
            k = i
            for k in range(i,j+1):
                sum += tab[k]
                k+=1
            s_max = max(s_max,sum)
    return s_max

tab = [randint(-20,20) for i in range(20)]
print(tab)
print(ssp3(tab))