import math
import time


def isprime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if x == 3:
        return True
    if x % 2 == 0:
        return False
    if x % 3 == 0 :
        return False
    
    for i in range(2,round(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


def truncprime(x):
    tempx = str(x)
    
    for i in range(0,len(tempx)):
        if not isprime(int(tempx[i:])):
            return False

    for i in range(len(tempx),0,-1):
        if not isprime(int(tempx[:i])):
            return False

    return True

start = time.time()
n = 0
Sum = 0
i = 10

while(n != 11):
    if truncprime(i):
        n += 1
        Sum += i
    i += 1

print('The answer is %s, found in %s seconds.' % (Sum,time.time() - start))
