Sum = 0

for i in range(1,1000):
    Sum += (i**i)

Sum = str(Sum)

print(Sum[-10:-1:1] + Sum[-1])
