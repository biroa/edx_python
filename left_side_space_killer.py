n = input('give me a string with spaces')

def left_side_space_killer(n):
    i=0
    while(ord(n[i])== 32):
        i+=1

    return(n[i:])

print(left_side_space_killer(n))
