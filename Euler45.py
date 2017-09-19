# Project Euler Problem 45: Triangular, pentagonal, and hexagon-
# -al
# By Yash Desai

import math
import time

start = time.time()

# Pentangonal checks whether x is a pentagonal number. This is
# done by solving the pentagonal formula using the quadratic
# formula. See wikipedia for notes. If the formula yields a nat-
# -ural number it means that the value x has that index in the
# sequence of pentagonal numbers. Since // division always ro-
# -unds down to an integer, and / division always returns a fl-
# -at, if the float of the // division is equal to the the value
# of the / division, the number must be a natural number.
def pentagonal(x):

    P = (1+math.sqrt(1+(24*x)))//6

    P2 = (1+math.sqrt(1+(24*x)))/6

    if P2 == float(P):
        return True

    else:
        return False

i = 2

# Since all hexagonal numbers are triangular, we can iterate th-
# -rough the hexagonal numbers and only have to check if the nu-
# -mbers are pentagonal. A quick search on my blog will lead yo-
# -u to the full explanation.
while True:

    i += 1
    # the formula below is the one that describes Hexagonal num-
    # -bers, ie. n(2n-1) for n >= 1
    candidate = i * ((2*i) - 1)

    # We are not interested in the value 40755 since the questi-
    # -on asks for the next hexagonal number that is also pent-
    # -agonal after 40755. To make the process faster you could
    # find what index 40755 has in the hexagonal numbers and st-
    # -art after that point.
    if pentagonal(candidate) and candidate != 40755:
        break

    
    
print('The answer is %s, solved in %s seconds' % (candidate,
        time.time() - start))
