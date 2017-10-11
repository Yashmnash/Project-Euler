# Project Euler Problem 49: Prime Permutations
# By Yash Desai

import itertools
import time
from math import sqrt 

def isprime(x):
    if x == 1:
        return False

    if x == 2:
        return True

    if x == 3:
        return True

    i = 0
    
    for i in range(2,round((x**0.5)+1)):
        if x % i == 0:
            return False

    return True

start = time.time()
Primes = set()

i = 0

for i in range(1000,10000):
    if isprime(i):
        Primes.add(i)


for i in Primes:

    T = False
    
    for j in Primes:

        if j <= i:
            continue
        
        k = j + (j-i)
        
        if k >= 10000 or not isprime(k):
            continue

        permutations = [''.join(x) for x in
                        list(itertools.permutations(str(i)))]
        

        if str(j) in permutations and str(k) in permutations:
            T = True
            break

    if T:
        break

print('The answer is %s, found in %s seconds' %
      (str(i) + str(j) + str(k), time.time() - start))
    
