# Project Euler Problem 56: Powerful digit sum
# By Yash Desai

from time import time

start = time()
largest = 0


# Finding the maximum digital sum of the value of a^b
# where a and b are two natural numbers below 100.
for a in range(1,100):
    for b in range(1,100):

        digits = [int(d) for d in str(a**b)]

        candidate = sum(Digits)

        if candidate > largest:
            largest = candidate


print('The answer is %s, found in %s seconds' % (largest,
        time() - start))
            
        
