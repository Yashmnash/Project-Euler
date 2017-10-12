import math
def isprime(x):
    for i in range(2,x):
        if x % i == 0:
            return 0
    return 1 

highprime = 1
num = int(math.sqrt(600851475143))


for i in (range(2,(num//2)+1)):
    print(i)
    if num % i == 0 and isprime(i) and i>highprime:
        highprime = i

print(highprime)
