import time

start = time.time()

terms = {4}


for a in range(2,101):
    for b in range(2,101):
        terms.add(a**b)

print('%s in %s sec' %(len(terms),time.time() - start))
