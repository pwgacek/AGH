def ssp2(tab):
    n = len(tab)
    s_max = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum+=tab[j]
            s_max=max(s_max,sum)
    return s_max


