import time

start = time.time()


List = []
Sum = set()

for i in range(1,10):
    List.append(str(i))

for a in range(1,100):
    for b in range(1,10000):
        c = a*b
        List2 = list(str(a) + str(b) + str(c))
        List2.sort()
        if List == List2:
            Sum.add(c)

print('The sum is %s, found in %s seconds' % (sum(Sum),time.time() - start))
            
