n = input('give a number between 0 and 10000: ')


def check_num(numeric):
    words_arr1 = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
    words_arr2 = ['','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    words_arr3 = ['hundred']
    words_arr4 = ['thousand']

    strLen = len(numeric)
    num = int(numeric)
    if(strLen == 1):
        char1= numeric[0]
        #print(char1)
    if(strLen == 2):
        char1= numeric[0]
        char2= numeric[1]
        #print(char1,char2)
    if(strLen == 3):
        char1= numeric[0]
        char2= numeric[1]
        char3= numeric[2]
        #print(char1,char2,char3)
    if(strLen == 4):
        char1= numeric[0]
        char2= numeric[1]
        char3= numeric[2]        
        char4= numeric[3]

        
    if(strLen <= 2):
        if(num<=20):
            print(words_arr1[num-1])
        else:
            if(char1 != '0' and char2 == '0'):
                print(words_arr2[int(char1)-1])
            else:
                print(words_arr2[int(char1)-1],words_arr1[int(char2)-1])

    elif(strLen == 3):
                if(char1 != '0' and char2 == '0' and char3 == '0'):
                    print(words_arr1[int(char1)-1],words_arr3[0])
                elif(char1 != '0' and char2 != '0' and char3 == '0'):
                    print(words_arr1[int(char1)-1],words_arr3[0],words_arr2[int(char1)-1])
                elif(char1 != '0' and char2 == '0' and char3 != '0'):
                    print(words_arr1[int(char1)-1],words_arr3[0],words_arr1[int(char3)-1])                    
                elif(char1 != '0' and char2 != '0' and char3 != '0'):
                    print(words_arr1[int(char1)-1],words_arr3[0],words_arr2[int(char2)-1],words_arr1[int(char2)-1])
        
    elif(strLen == 4):
                if(char1 != '0' and char2 == '0' and char3 == '0' and char4 == '0'):
                    print(words_arr1[int(char1)-1],words_arr4[0])
                elif(char1 != '0' and char2 != '0' and char3 == '0' and char4 == '0'):
                    print(words_arr1[int(char1)-1],words_arr4[0],words_arr1[int(char2)-1],words_arr3[0])
                elif(char1 != '0' and char2 != '0' and char3 != '0' and char4 == '0'):
                    print(words_arr1[int(char1)-1],words_arr4[0],words_arr1[int(char2)-1],words_arr3[0],words_arr2[int(char3)-1])
                elif(char1 != '0' and char2 != '0' and char3 != '0' and char4 != '0'):
                    print(words_arr1[int(char1)-1],words_arr4[0],words_arr1[int(char2)-1],words_arr3[0],words_arr2[int(char3)-1],words_arr1[int(char4)-1])

        
        
check_num(n)
