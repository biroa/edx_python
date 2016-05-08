def get_char(string):
    summ = 0
    i=0
    while(i<len(string)):
        summ+=ord(string[i])
        i+=1
    return summ

print(get_char("hello"))

