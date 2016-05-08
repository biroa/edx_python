# Type your code here
# s1 string
# s2 list

import string

alphabet = list(string.ascii_lowercase)


def string_to_list(s1):
    arr = s1.split()
    return arr

def equal(str1,str2):
    if(str1==str2):
        return True

    return False

def insert_and_compare(str1,str2):
    #print('insert_and_compare',str1,str2)
    for x in alphabet:
        newStr = str1
        for j in range(0,len(str1)+1):
            index = j
            result = newStr[:index] + x + newStr[index:]
            #print('insert_and_compare',j,index,result)
            if(result == str2):
                #print('insert_and_compare',result)
                return True
            
    return False
        
        
def delete_and_compare(str1,str2):
    #print('delete_and_compare',str1,str2)
    newStr = str1
    for j in range(0,len(str1)+1):
        index = j
        result = newStr[:index] + newStr[(index+1):]
        #print('delete_and_compare',j,index,result)
        if(result == str2):
            print('delete_and_compare',result)
            return True

    return False

def spelling_corrector(s1,s2):
    string1= s1.lower()
    string2= s2
    output_string = []
    s1Arr = string_to_list(string1)
    for i in range(0,len(s1Arr)):
        if(len(s1Arr[i])>2):
            #We do not check characters shorter length than two
            counter = 0
            for j in range(0,len(string2)):
                #print(s1Arr[i])
                if(i==0 and j == 0):
                    output_string.append(s1Arr[i])
                    break
                elif(equal(s1Arr[i],string2[j])):
                    output_string.append(string2[j])
                    break
                elif(insert_and_compare(s1Arr[i],string2[j]) or delete_and_compare(s1Arr[i],string2[j])):
                    print(s1Arr[i],string2[j])
                    output_string.append(string2[j])
                    break
                elif(len(string2[j])==counter):
                    #print('nothing went well',s1Arr[i],string2[j])
                    output_string.append(s1Arr[i])
                    break
                counter += 1        
                    
        else:
            output_string.append(s1Arr[i])
            continue


    
    return (' ').join(output_string)

#print(spelling_corrector('Thes is the Firs cas',['that','first','case','car']))
print(spelling_corrector('Asignment three xample inpu ', ['Assignmen', 'tree', 'three', 'example', 'output', 'input']))
#spelling_corrector('programing is fan and easy',['programming','this','fun','easy','book' ])
