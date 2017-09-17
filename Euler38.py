# Project Euler Problem 38: Pandigital multiples
# By Yash Desai

import itertools
import time

start = time.time()

# Initialize a set called pandigitals which contains all the 1-9
# pandigital numbers.
pandigitals = set([''.join(x) for x in
                   list(itertools.permutations(
                    ['1','2','3','4','5','6','7','8','9']))])

largest_pandigital = 0

# The concatenated product of a four digit number and two one
# digit numbers will yield 9 digits. Thus the maximum for the
# first integer is 9999, the maximum four digit number.
for i in range(1,10000):

    candidate = '' 

    for j in range(1,10):

        # Concatenate the product
        candidate += str(i * j)

        # If the number is already long enough to be pandigital,
        # is pandigital, and exceeds the largest one already fo-
        # -und, update the largest value.
        if (candidate in pandigitals and
            int(candidate) > largest_pandigital):

            largest_pandigital = int(candidate)
            
    

print('The answer is %s, found in %s seconds' %(largest_pandigital
        ,time.time() - start))
