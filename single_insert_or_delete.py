import string

alphabet = list(string.ascii_lowercase)


def equal(str1,str2):
    if(str1==str2):
        return True

    return False

def insert_and_compare(str1,str2):
    for x in alphabet:
        newStr = str1
        for j in range(0,len(str1)+1):
            index = j
            result = newStr[:index] + x + newStr[index:]
            #print(j,index,result)
            if(result == str2):
                #print(result)
                return True
            
    return False
        
        

def delete_and_compare(str1,str2):
    newStr = str1
    for j in range(0,len(str1)+1):
        index = j
        result = newStr[:index] + newStr[(index+1):]
        #print(j,index,result)
        if(result == str2):
            #print(result)
            return True

    return False
            


# Type your code here
def single_insert_or_delete(s1,s2):
    str1=s1.lower()
    str2=s2.lower()
    if(equal(str1,str2)):
        return 0
    elif(insert_and_compare(str1,str2) or delete_and_compare(str1,str2) ):
        return 1
    else:
        return 2
            


#print(insert_and_compare('alma','almak'))
print(single_insert_or_delete('alma','almak'))

