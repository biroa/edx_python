def crazy_list(some_list):

    arr_length = len(some_list)
    item = 1
    for i in range(0,arr_length):
        
        if(some_list[i] != some_list[arr_length-item]):
            return False
        item+=1

    return True

print(crazy_list([4, 5, 6, 7, 8, 4, 5, 2]))
        

        
