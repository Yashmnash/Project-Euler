f = open('p022_names.txt')
f = str(f.read())

List = f.split(",")
List = sorted(List)

Sum = 0
Product = 0

for i in range(0,len(List)):
    Sum = 0
    for j in range(1,len(List[i]) - 1):
        Sum += ord(str(List[i][j])) - 64

    Product += (Sum * (i+1))

print(Product)
