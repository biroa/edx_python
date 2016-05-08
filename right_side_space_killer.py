n = input('give me a string with spaces')

def left_side_space_killer(n):
    length = len(n)
    idx = 0
    i=-1*(len(n))
    print(i)
    end=-1
    while(end>=i):
        print(n[i])
        if(ord(n[i])!=32):
            print(n[i],i)
            break
        i+=1

    print(i)
    return n[-1:i]
        


        
print(left_side_space_killer(n))
