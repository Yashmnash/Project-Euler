def palin(x):
    x = str(x)
    for i in range(0,len(x)):
        if x[i] != x[-i-1]:
            return False

    return True



Sum = 0

for i in range(1,1000001):
    binary = bin(i)[2:]
    if palin(i) and palin(binary):
        Sum += i

print(Sum)
