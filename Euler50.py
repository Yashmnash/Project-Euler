# Project Euler Problem 50: Consecutive prime sum
# By Yash Desai

from math import sqrt
from time import time

def isprime(x):
    if x == 2 or x == 3:
        return True
    elif x % 2 == 0:
        return False
    elif x % 3 == 0:
        return False

    for i in range(5, int(sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True

start = time()

sum = 0
i = 1
primes = []

# This loop generates a list of consecutive primes such that the
# sum of all the primes is less than 1,000,000
while(sum<1000000):
    if isprime(i):
        sum += i
        primes.append(i)

    i += 1

# clears the sum 
del sum

# The first loop changes the length of consecutive sum. For exam
# -ple, it starts at two so possible consecutive sums could be
# 2,3 = 5. The second loop iterates through the list of primes
# to find all possible consecutive sums of length i. Finally
# the sum is tested for primality. Since the length of the
# consecutive sum is always increasing, the loops will finish
# with the largest possible prime under 1,000,000.
for i in range(2,len(primes)):
    for j in range(0,len(primes) - i):
        candidate = sum(primes[j:j+i])
        if isprime(candidate):
            longest = candidate


print('The answer is %s, found in %s seconds' %
        (longest,time() - start))
    
        
    
    
