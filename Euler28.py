
Sum = 1
Number = 1
indent = 2

for i in range(3,1002,2):
    for j in range(4):
        Number = Number + indent
        Sum += Number

    indent += 2

print(Sum)
