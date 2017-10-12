def isprime(x):
    if x == 0:
        return False
    if x == 1:
        return False
    if x == 2:
        return True
    if x == 3:
        return True
    for i in range(2,round((x**0.5)+1)):
        if x % i == 0:
            return False
        else:
            continue

    return True

Max = 0
Primes = set()

for i in range(1,100):
    if isprime(i):
        Primes.add(i)

for b in range(-1000,1001):
    for a in range(-999,1000):
        n = 0
        candidate = (n**2) + (a*n) + b

        if candidate < 0:
            continue

        while(candidate in Primes):
            n += 1
            candidate = (n**2) + (a*n) + b
            # Can create a max test to not rely on arbitrary upper limit to the set 'Primes'
            # ie. see if new candidate exceeds max, and if so test for primality and add to set if so.
            if candidate > max(Primes):
                if isprime(candidate):
                    Primes.add(candidate)
            

        if n > Max:
            Max = n
            A = a
            B = b

print(A*B)
