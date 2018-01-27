# Project Euler Problem 52: Permuted multiples
# By Yash Desai

import time

start = time.time()
candidate = 1
digits = []


while(True):

    digits.append(set(str(candidate)))

    # This loop creates sets of the digits of the multiples of
    # the integer i in question, and adds it to a list.
    for j in range(2,7):
        digits.append(set(str(j*candidate)))

    # This checks if all the elements in digits are identical  
    if digits == digits[::-1]:
        break

    candidate += 1
    digits = []

print('The answer is {}, found in {:.2f} seconds'.format(
        candidate,time.time() - start))

    
