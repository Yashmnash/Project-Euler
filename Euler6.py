SSquare = 0
for i in range(1,101):
    SSquare += (i*i)

SquareS = 0
for i in range(1,101):
    SquareS += i

SquareS = SquareS*SquareS

print(SquareS - SSquare)
