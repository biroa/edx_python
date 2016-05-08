def pattern_sum(a, b):
    length = b+1
    result=[]
    for i in range(1,length):
        if(i==1):
            result.append(a)
        else:
            item = ''
            for j in range(1,i+1):
                item = item + str(a)
            result.append(int(item))

    return sum(result)
print(pattern_sum(4,5))
