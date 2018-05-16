# Project Euler Problem 79: Passcode derivation
# By Yash Desai

from time import time

start = time()

file = open("C:/Users/Yash/AppData/Local/Programs/Python/Python36/p079_keylog.txt", 'r')

# Nums holds all numbers from the login attempts
Nums = []

for line in file.readlines():

    Nums.append(line[0:-1])

# This removes duplicates 
Nums = list(set(Nums))

# Holds the possible digits of the passcode
Digits = []

# These loops get all feasbile digits from Nums
for i in Nums:
    for j in i:
        
        if j not in Digits:
            Digits.append(j)

        else:
            continue

# This loop does the following: For each login attempt, if a nu-
# mber appears in a different relative ordering compared to Dig-
# its, the two numbers in Digits are swapped. The first and sec-
# ond, second and third, and first and second numbers of the at-
# tempt are compared.
for j in Nums: 
        
        a = Digits.index(j[0])
        b = Digits.index(j[1])
        c = Digits.index(j[2])

        if a > b:
            Digits[a], Digits[b] = Digits[b], Digits[a]

        if b > c:
            Digits[b], Digits[c] = Digits[c], Digits[b]

        if a > c:
            Digits[a], Digits[c] = Digits[c], Digits[a]

print('The answer is %s, found in %s seconds.' %
      (''.join(Digits),time()-start))
            
            
        
        
        
