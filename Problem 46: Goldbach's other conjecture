# Project Euler Problem 46: Goldbach's other conjecture
# By Yash Desai

import time
import math

def isprime(x):
    
    if x == 1:
        return False

    if x == 2:
        return True

    if x == 3:
        return True

    for i in range(2,round(math.sqrt(x))+1):
        if x % i == 0:
            return False

    return True

Primes = set()

for i in range(1,10000):
    if isprime(i):
        Primes.add(i)

Squares = set()

for j in range(1,10000):
    Squares.add(j)

Evens = set()

for k in range(2,10000):
    if k % 2 == 0:
        Evens.add(k)

Composites = Squares - Evens - Primes - {1}

B1 = False
Composites2 = set(Composites)

for i in Composites:
    B1 = False
    B2 = False
    for j in Primes:
        for k in Squares:
            candidate = j + (2*(k**2))

            if i == candidate:
                B1 = True
                B2 = True
                break
        if B1:
            break

    else:
        break

    
print(i)
    
