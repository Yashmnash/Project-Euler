# Project Euler Problem 40: Champernowne's constant
# By Yash Desai

import time

start = time.time()

i = 1
digits = ''
product = 1

# This loop adds sequential natural numbers to a string until
# the length of the string is 1,000,000, which is the highest
# digit needed in the computation of the product.
while(len(digits) <= 1000000):

    digits = digits + str(i)
    
    i += 1

# This loop finds the product of the digits with indices equal
# to powers of ten up to 1,000,000
for i in [0,9,99,999,9999,99999,999999]:
    product *= int(digits[i])


print('The answer is %s, found in %s seconds' % (product,
        time.time() - start))
    
