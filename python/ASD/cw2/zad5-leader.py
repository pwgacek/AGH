def find_candidate(T):
    n = len(T)
    bilans = 1
    current_candidate = T[0]

    for i in range(1,n):
       
        
        if T[i] == current_candidate:
            bilans+=1
        else:
            bilans-=1

        if bilans == 0:
            current_candidate = T[i]
            bilans = 1
    return current_candidate 

def is_leader(T,current_candidate):
   
    n = len(T)
    counter = 0
    for i in range(n):
        if T[i] == current_candidate:
            counter+=1
        
    if counter > n // 2:
        return True 
    
    return False

def leader(T):
    candidate  = find_candidate(T)
    return is_leader(T,candidate)

        

T = [4,4,1,1,1,4,1,2,4]
print(leader(T))
