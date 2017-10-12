import math
import time


def isprime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if x == 3:
        return True

    for i in range(2,round(math.sqrt(x)) +1):
        if x % i == 0:
            return False

    return True

def switch(x):
    Circular = {x}
    x = list(str(x))
    tempx = x[:]
    while(True):
        tempx = tempx[1:len(tempx)] + tempx[0:1]
        if tempx == x:
            return list(Circular)
        Circular.add(int(''.join(tempx)))
   

start = time.time()

Primes = {2}
for i in range(1,1000000):
    if isprime(i):
        Primes.add(i)

number = 0

for i in Primes:
    List = switch(i)
    count = 0
    for j in List:
        if j in Primes:
            count +=1

    if count == len(List):
        number += 1

print('The answer is %s found in %s seconds' % (number,time.time() - start))       
    
