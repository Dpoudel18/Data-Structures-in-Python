def rearrange_recur(L, first, last):
    if first == last:
        return L
    elif L[first] % 2 == 1 and L[last] % 2 == 0:
        L[first], L[last] = L[last], L[first]
        return rearrange_recur(L, first+1, last-1)
    elif L[first] % 2 == 1:
        return rearrange_recur(L, first, last-1)
    else:
        return rearrange_recur(L, first+1, last)

def rearrange(L):
    return rearrange_recur(L, 0, len(L)-1)

    