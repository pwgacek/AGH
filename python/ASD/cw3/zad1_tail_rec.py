def quick_sort(T,p,r):

    while p < r :
        pivot = partition(T,p,r)

        if (pivot - p) < (r - pivot):
            quick_sort(T,p,pivot-1)
            p = pivot + 1
        else:
            quick_sort(T,pivot+1,r)
            r = pivot - 1