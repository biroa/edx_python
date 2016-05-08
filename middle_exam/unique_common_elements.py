import operator
def unique_common(a, b):
    result = set(a).intersection(b)
    if(len(result)>0):
         return sorted(result)
    else:
        return 'None'

print(unique_common([5, 6, 7, 0], [3, 2, 3, 2]))
