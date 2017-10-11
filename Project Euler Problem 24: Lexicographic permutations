# Project Euler Problem 24: Lexicographic permutations
# By Yash Desai

import itertools
import time

start = time.time()

# Generate a list of the permutations of the digits 0-9, and re-
# -trieve the tuple at the 1,000,000th index.

item = list(itertools.permutations(['0','1','2','3','4','5','6',
        '7','8','9']))[999999]

# ''.join() is used to combine the elements of the tuple into a
# single number.

print('The answer is %s,found in %s seconds' % (''.join(item),
        time.time() - start))
