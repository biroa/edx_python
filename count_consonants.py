# Type your code here
def count_consonants(string):
    lcString= string.lower()
    counter = 0
    for x in lcString:
        if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
            counter+=1


    return counter
    
