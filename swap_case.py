
def _swap_cases(n):
    result=''
    i=0
    while(i<len(n)):
        if(ord(n[i]) > 63 and ord(n[i]) < 91 ):
            result += chr(ord(n[i])+32)
        elif(ord(n[i]) > 96 and ord(n[i]) < 123):
            result += chr(ord(n[i])-32)
        else:
            result +=n[i]
        i+=1
    return result

print(_swap_cases("Al Ma"))
