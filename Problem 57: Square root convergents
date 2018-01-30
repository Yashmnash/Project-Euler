# Project Euler Problem 57: Square root convergents
# By Yash Desai

# 3/2 is an initial guess for the square root of 2
p = 3
q = 2
count = 0

# The formula below uses the recursive formula for the root of 2
for i in range (2,1001):

    p,q = 2*q + p, q + p

    if len(str(p)) > len(str(q)):
        count += 1


print(count)

