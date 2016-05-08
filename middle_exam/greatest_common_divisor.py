import fractions

def myreduce(fnc, seq):
    tally = seq[0]
    for next in seq[1:]:
        tally = fnc(tally, next)
    return tally

def find_gcd(some_list):
    return myreduce(fractions.gcd, some_list)


print(find_gcd([3, 5, 9, 11, 13]))
