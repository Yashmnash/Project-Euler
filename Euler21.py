def d(x):
    F = [1]
    i = 2

    while(i < round(x**0.5)+ 1):
        if x % i == 0:
            F.append(i)
            if not x//i in F:
                F.append(x//i)

        i += 1

    Sum = 0
    
    for i in F:
        Sum += i

    return Sum


A = []

for i in range(0,10000):
    b = d(i)
    if d(b) == i and b != i and d(i) < 10000 and i not in A and b not in A:
        A.append(i)
        A.append(b)
        

Sum = 0

for i in A:
    Sum += i

print('The sum of all the amicable numbers under 10,000 is %s' % (Sum))
        
        
