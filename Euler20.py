#Euler20


Product = 1

for i in range(1,101):
    Product *= i


Sum = 0

for i in str(Product):
    Sum += int(i)

print(Sum)
