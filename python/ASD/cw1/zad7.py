def find(T,x):
    l = 0
    p = len(T) - 1

    while l < p :
        if T[l] + T[p] == x: 
            return True

        elif T[l] + T[p] < x:
            l+=1
        else:
            p-=1

    return False
