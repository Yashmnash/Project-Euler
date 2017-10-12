import time
import math

def isprime(n):
    if n == 1:
        return False
    elif n<4:
        return True
    elif n%2 == 0:
        return False
    elif n<9:
        return True
    elif n%3 == 0:
        return False
    else:
        f = 5
        while f*f<= n:
            if n%f == 0:
                return False
            if n%(f+2) == 0:
                return False
            f += 6
        return True

def is_prime(n):
    if n%2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 2
    return True

def nth_prime(n,func):
    prime = 2
    count = 1
    iter = 3

    while(count<n):
        if func(iter):
            prime = iter
            count += 1
        iter += 2
    return prime

start = time.time()
prime = nth_prime(10001,is_prime)
elapsed = (time.time() - start)

print('founds %s in %s seconds' %(prime, elapsed))

start = time.time()
prime = nth_prime(10001,isprime)
elapsed = (time.time() - start)

print('founds %s in %s seconds' %(prime, elapsed))
