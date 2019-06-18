def merge_sortedarrays(my_array1, my_array2): 
    
    size_1=len(my_array1)
    size_2=len(my_array2)
    
    my_array3 = [None] * (size_1 + size_2) 
    
    a = 0
    b = 0
    c = 0
    
    while a < size_1 and b < size_2: 

        if my_array1[a] < my_array2[b]: 
            my_array3[c] = my_array1[a] 
            c += 1
            a += 1
            
        else: 
            my_array3[c] = my_array2[b] 
            c += 1
            b += 1
      
    while a < size_1: 
        my_array3[c] = my_array1[a]; 
        c += 1
        a += 1

    while b < size_2: 
        my_array3[c] = my_array2[b]; 
        c += 1
        b += 1
    
    return my_array3
