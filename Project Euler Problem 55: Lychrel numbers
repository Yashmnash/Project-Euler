# Project Euler Problem 55: Lychrel numbers
# By Yash Desai

import time

# This function checks if an int is a palindrome
def ispalindrome(x):

    A = list(str(x))

    if A == A[::-1]:
        return True

    else:
        return False

# This function reverses integers
def reverse(x):

    A = list(str(x))
    return int(''.join(A[::-1]))

start = time.time()
# Initial count for Lychrel numbers
count = 0

for i in range(1,10000):

    # temp is the potential palindrome
    temp = i + reverse(i)
    # j is the number of iterations
    j = 0
    
    while(j<50):

        if ispalindrome(temp): 
            break
        else:
            j += 1

        temp = temp + reverse(temp)

    if j == 50:
        # If the number of iterations exceeded 49, it is consid-
        # -ered a Lychrel number
        count += 1

end = time.time()

print('The answer is {}, found in {:.2f} seconds'.format(count,
        end - start))
    
