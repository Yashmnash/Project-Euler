import time

def collatz(stnum):
    n = stnum
    count = 1

    while(n != 1):
        if n%2 == 0:
            n = n//2
            count += 1

        else:
            n = (3*n) + 1
            count += 1

    return count

start = time.time()
candidate = 1
highest = 0
highestcandidate = 0

while(candidate < 1000000):
    length = collatz(candidate)
    if length > highest:
        highest = length
        highestcandidate = candidate
        candidate += 1

    else:
        candidate += 1



total = time.time() - start
print('The answer is %s and it took %s seconds' % (highestcandidate, total))