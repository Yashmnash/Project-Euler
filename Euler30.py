List = []

for i in range(2,355000):
    digits = [int(k) for k in str(i)]
    Sum = 0
    for j in digits:
        Sum += j**5
    if i == Sum:
        List.append(i)


print(sum(List))
    
