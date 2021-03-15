from time import time
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




def ssp1_5(tab, l, p):
    if l>p: return 0
    if l==p: return max(0,tab[l])
    sr = (l+p)//2
    wl = ssp1_5(tab,l,sr)
    wp = ssp1_5(tab,sr+1,p)
    sl = sp = 0
    par = 0
    for i in range(sr+1,p+1):
        par += tab[i]
        if par>sp: sp = par

    par = 0
    for i in range(sr,l-1,-1):
        par += tab[i]
        if par>sl: sl = par

    return max(wl,wp,sl+sp)





def ssp2(tab):
    n = len(tab)
    s_max = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum+=tab[j]
            s_max=max(s_max,sum)
    return s_max











def ssp1(tab):
    n = len(tab)
    s_max = 0 
    sum = 0
    for i in range(n):
        sum+=tab[i]
        if sum < 0 : sum = 0
        s_max = max(s_max,sum)
    return s_max






















tab= [randint(-1000,1000) for i in range(1000)]

start=time()
print(ssp1(tab))
end=time()

total= end - start
print("srt_lin: {0:02f}s".format(total))



start=time()
print(ssp1_5(tab,0,len(tab)-1))
end=time()

total= end - start
print("srt_nlogn:{0:02f}s".format(total))



start=time()
print(ssp2(tab))
end=time()

total= end - start
print("srt_kwad: {0:02f}s".format(total))



start=time()
print(ssp3(tab))
end=time()

total= end - start
print("srt_szesc: {0:02f}s".format(total))
