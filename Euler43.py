# Project Euler Problem 43: Sub-string divisibility
# By Yash Desai

import itertools
import time

start = time.time()


Primes = {2,3,5,7,11,13,17}

# substring takes a pandigital number as a string and checks if
# it meets the substring divisibility property 
def substring(x):

    # itertate through successive three digits and check if they
    # can be divided by successivley larger primes
    for i,j in zip(Primes,range(1,8)):

        if int(x[j:j+3]) % i == 0:
            
            continue
                
        else:
            return False


    return True


pandigitals = []

# For all the permutations of the ten digits, find the ones that
# do not have a leading zero, and add them to a list called pan-
# -digitals that stores all the pandigital numbers.
for x in itertools.permutations(['0','1','2','3','4','5','6','7',
                                '8','9']):
    if x[0] == '0':
        
        continue
    
    else:
        pandigitals.append(''.join(x))

Sum = 0

# Iterate through the pandigital numbers and check if they meet
# the substring divisibility property. If so, add it to Sum.
for i in pandigitals:

    if substring(i):
        
        Sum += int(i)

print('The answer is %s, found in %s seconds' % (Sum,time.time() - start))       
