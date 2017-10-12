import time

def abundant(x):

    F = [1]
    i = 2

    while(i< round(x**0.5) + 1):
        if x % i == 0:
            F.append(i)
            if not x//i in F:
                F.append(x//i)

        i += 1
    
    Sum = sum(F)

    if Sum > x:
        return True

    else:
        return False

start = time.time()

A = []
Integers = [x for x in range(1,28124)]
Numbers = []

for i in range(1,28124):
    if abundant(i):
        A.append(i)

for i in A:
    j = 0
    Sum = i + A[j]
    while(Sum < 28124):
        Numbers.append(Sum)    
        j += 1
        Sum = i + A[j]


List = set(Integers) - set(Numbers)

print('The answer is %s and it was done in %s seconds' % (sum(List),(time.time() - start)))

        
        
