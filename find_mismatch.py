def equal(str1,str2):
    if(str1==str2):
        return True

    return False

#return length equality
def is_same_length(str1,str2):
    if(len(str1)==len(str2)):
        return True

    return False

#return num of mismatch
def mismatch_num(str1,str2):
    mismatch=0
    for i in str1:
        x=str2.count(i)
        if(x==0):
            mismatch+=1

    return mismatch

def find_mismatch(s1,s2):
    str1=s1.lower()
    str2=s2.lower()
    if(equal(str1,str2)):
        return 0
    elif(is_same_length(str1,str2) and mismatch_num(str1,str2)==1):
        return 1
            
    elif(is_same_length(str1,str2) == False or mismatch_num(str1,str2)>=2):
        return 2
        
        
    
