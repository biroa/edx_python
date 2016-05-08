import math
# Returns a list of prime numbers calculated using
# the Sieve of Eratosthenes algorithm.

def list_of_primes(n):
    sieve = [True] * n
    sieve[0] = False # zero and one are not prime numbers
    sieve[1] = False

    # create the sieve
    for i in range(2, int(math.sqrt(n)) + 1):
        pointer = i * 2
        while pointer < n:
            sieve[pointer] = False
            pointer += i

    # compile the list of primes
    primes = []
    for i in range(n):
        if sieve[i] == True:
            primes.append(i)

    return primes

print(list_of_primes(100))
