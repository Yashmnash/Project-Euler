import time

start = time.time()
pent_num = set()
for i in range(1,10000):
    pent_num.add(int(i * ((3*i) -1) * 0.5))



B = False

for k in pent_num:
    for j in pent_num:
        if j == k:
            continue
        if k+j in pent_num and abs(k-j) in pent_num:
            B = True
            Answer = abs(k-j)
            break

    if B:
        break

print('The answer is %s, made with the pair %s and %s found in %s seconds' % (Answer,k,j,time.time()-start))
            
        
