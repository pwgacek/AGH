def find_min_max(T):
    n=len(T)
    x_min = x_max = T[0] 

    if n % 2 == 0 : 
        #parzysta liczba elementow
        for i in range(0,n,2):
            if T[i] < T[i+1]:
                x_min = min(x_min,T[i])
                x_max = max(T[i+1],x_max)
            else :
                x_min = min(x_min,T[i+1])
                x_max = max(T[i],x_max)

        return x_min,x_max

    else:
        

        for i in range(0,n-1,2):
            if T[i] < T[i+1]:
                x_min = min(T[i],x_min)
                x_max = max(T[i+1],x_max)
            else :
                x_min = min(T[i+1],x_min)
                x_max = max(T[i],x_max)

        x_min = min(T[n-1],x_min)
        x_max = max(T[n-1],x_max)

        return x_min,x_max

print(find_min_max([3,4,5,6,6,3,4,22,2,3,2]))