import math

def sumfacdig(x):
    Sum = 0
    for i in str(x):
        Sum += math.factorial(int(i))

    return Sum


Sum = 0

for i in range(10,2540161):
    if sumfacdig(i) == i:
        Sum += i

print(Sum)
