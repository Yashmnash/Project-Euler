# Project Euler Problem 2: Even Fibonacci numbers
# By Yash Desai

# The list A is a list that will hold the fibonacci numbers.
A = [1,2]
n = 2
sum = 2

while(A[-1] <= 4000000):
    A.append(A[n-2] + A[n-1])

    # if the latest fibonacci number is even, add it to the sum.
    if A[n] % 2 == 0:
        sum += A[n]
    n += 1
    print(n)

print(sum)
