import time


def primefactor(x):
    
    Factors = set()

    
    i = 2

    while(i <= x**0.5 or x  == 1):
        if x%i == 0:
            Factors.add(i)
            x = x//i
            i -= 1

        i += 1
        
           
    return (len(Factors) + 1)


start = time.time()

i = 210

while(True):

    if primefactor(i) == 4:
        i += 1
        if primefactor(i) == 4:
            i += 1
            if primefactor(i) == 4:
                i += 1
                if primefactor(i) == 4:
                    break

    i += 1            

print('Answer is %s, finished in %s seconds' % (i-3,time.time() - start))
