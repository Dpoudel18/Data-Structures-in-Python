# A python function to print all the distinct elements of the array.

def distinct_elements(my_array): 
    for i in range(len(my_array)): 
        repeat = 1
        for j in range(0, i): 
            if (my_array[i] == my_array[j]): 
                repeat = 2 
                break
        if (repeat == 1): 
            print(my_array[i]) 