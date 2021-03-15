def ssp1_5(tab, l, p):
    if l>p: return 0
    if l==p: return max(0,tab[l])
    sr = (l+p)//2
    wl = ssp2(tab,l,sr)
    wp = ssp2(tab,sr+1,p)
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