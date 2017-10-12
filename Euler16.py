import time

start = time.time()
A = str(2**1000)
Sum = 0

for i in A:
    Sum += int(i)

elapsed = time.time() - start

print(Sum,elapsed)
