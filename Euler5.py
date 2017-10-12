def prod(A):                #Returns product of terms of iterable
    product = 1
    for i in A:
        product *= i
    return product

def isprime(x):             #Checks primality
    for i in range(2,x):
        if x%i == 0:
            return False
        else:
            continue
    return True

def lowestprimefactor(x):   #Return the lowest prime factor 
    for i in BasePrime:
        if x%i == 0:
            return i
        else:
            continue

Upto = int(input('Please enter the upper limit: '))

P = []
F = []

for i in range(2,Upto+1):   #Assigning to P the prime factors 
    if isprime(i):          #Assigning to F the non-prime factors
        P.append(i)
    else:
        F.append(i)


BasePrime = P[::]           #Two copies of inital P and F
BaseFactor = F[::]

for i in BaseFactor:        
    if prod(P)%i == 0:      #If a non-prime factor in F can already be made from the multiple of primes in P, take it out of F
        F.remove(i)
    else:                   #Else, it can't be made. Add it's lowest prime to the list of primes.
        P.append(lowestprimefactor(i))

print(prod(P))

