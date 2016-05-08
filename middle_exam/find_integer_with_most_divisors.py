def divisors(num):
    divisors_num = 0
    divisors = []
    for i in range(1,num+1):
        if num % i == 0:
            divisors_num+=1
            divisors.append(i)


    #print(divisors,divisors_num)
    return divisors_num

def get_the_first_highest_index(arr):
    i=0
    max = 0
    while(i<len(arr)):
        if(arr[i]> max):
            max=arr[i]
            max_index = i
        i+=1
    return max_index

def find_integer_with_most_divisors(input_list):
    i=0
    all_divisors = []
    while(i<len(input_list)):
        #print(input_list[i])
        all_divisors.append(divisors(input_list[i]))
        i+=1

    return(input_list[get_the_first_highest_index(all_divisors)])


find_integer_with_most_divisors([8, 12, 18, 6])
