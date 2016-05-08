# Type your code here
def test_for_anagrams(my_string1, my_string2):
    counter=0;
    new_str1=my_string1.lower()
    new_str2=my_string2.lower()
    for x in new_str1:
        for j in new_str2:
            #print(x,my_string1,j,new_str2,len(new_str2))
            if(x == j):
                counter+=1
                new_str2 = new_str2 .replace(x, "")
                break
    

    if(len(new_str2) == 0):
        return True

    return False

print(test_for_anagrams('pupil','tuple'))
#print(test_for_anagrams('Orchestra','Carthorse'))
