# Project Euler Problem 57: Square root convergents
# By Yash Desai

p = 5
q = 1
count = 0

for i in range (2,10):

    p,q = 2*q + p, q + p

    if len(str(p)) > len(str(q)):
        count += 1


print(count)
print(p/q)
