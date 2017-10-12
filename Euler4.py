def ispalindrome(x):
    X = list(str(x))
    for i in range(0,len(X)):
        if X[i] == X[-i-1]:
            continue
        else:
            return False
    return True


Product = 1

for i in range(100,999):
    for j in range(100,999):
        if ispalindrome(i*j) and i*j>Product:
            Product = i*j

print(Product)
