# Type your code here
def my_encryption(some_string):
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
    counter = 0
    newStr=''
    for i in some_string:
        found = 0
        for j in character_set:
            if(i == j):
                ind=character_set.index(i)
                newStr += secret_key[ind];
                #print(j,i,ind,secret_key[ind],newStr)
                found=1

        if found == 0:
            return False


    return newStr



print(my_encryption('Lets meet at the usual place at 9 am'))
