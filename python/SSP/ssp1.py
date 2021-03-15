def ssp1(tab):
    n = len(tab)
    s_max = 0 
    sum =0
    for i in range(n):
        suma+=tab[i]
        if suma < 0 : suma = 0
        s_max = max(s_max,sum)
    return s_max

