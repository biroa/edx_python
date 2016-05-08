def find_longest_word(some_string):
    chars = some_string.split()
    longest = '';
    for x in chars:
        longest = x;
        if(len(longest)<= len(x)):
            longest = x
    return longest
    

print(find_longest_word("This is a test for meee"))
