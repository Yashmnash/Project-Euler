# Project Euler Problem 41: Pandigital prime
# By Yash Desai

import math
import itertools
import time


"""npandigital takes a number, x, and returns all n-pandigital
numbers with length x in a list. Eg. x = 2 will yield,
[(1,2),(2,1)]"""

def npandigital(x):
    
    Digits = ['1','2','3','4','5','6','7','8','9']
    
    # We are choosing the x first digits from the list Digits
    # and permuting them.
    List_of_permutations = list(itertools.permutations(list(Digits[0:x])))

    return List_of_permutations

"""isprime tests the primality of a number x"""

def isprime(x):
    
    if x == 1:
        return False
    if x == 2:
        return True
    if x == 3:
        return True

    for i in range(2,round(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True

start = time.time()

# npandigital_numbers is a list of all n-pandigital numbers

npandigital_numbers = []

# largest_prime is a store for the largest n-pandigital number
# that is also prime.
largest_prime = 2

# This generates all n-pandigital numbers (digits 1-9)
for i in range(1,10):
    
    npandigital_numbers.append(npandigital(i))

    
# Since the n-pandigital function returns a list of tuples, to
# obtain a specific n-digit number from npandigital_numbers we
# have to run through two loops, and then join the elements in
# each tuple.
for i in range(len(npandigital_numbers)):
    
    for j in range(len(npandigital_numbers[i])):

        candidate = int(''.join(npandigital_numbers[i][j]))

        if isprime(candidate) and candidate > largest_prime:
            largest_prime = candidate
            
print('The answer is %s, found in %s seconds' % (largest_prime,
        time.time() - start))
      
    
