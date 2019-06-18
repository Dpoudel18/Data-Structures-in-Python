def find_min_max_recur(L,minimum,maximum):
    if len(L)==0:
        return minimum, maximum
    if L[0]>maximum:
        maximum=L[0]
    if L[0]<minimum:
        minimum=L[0]
    return find_min_max_recur(L[1:],minimum,maximum)

def find_min_max(L):
    if len(L)==0:
        raise ValueError ("Empty List")
    minimum = L[0]
    maximum = L[0]
    minimum,maximum = find_min_max_recur(L,minimum,maximum)
    return minimum,maximum