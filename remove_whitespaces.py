
def _remove_white_spaces(n):
    result=''
    i=0
    while(i<len(n)):
        print(ord(n[i]),n[i])
        if(ord(n[i]) != 32):
            result += n[i]
            print(result)
            
        i+=1
    return result

print(_remove_white_spaces("  al ma   "))
