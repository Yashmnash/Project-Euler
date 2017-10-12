import time

def route_num(cube_size):
    L = [1] * cube_size
    for i in range(cube_size):
        print('i: %s' % i)
        for j in range(i):
            print('j: %s' % j)
            print('L[j] + L[j-1] = %s + %s' % (L[j],L[j-1]))
            time.sleep(4)
            L[j] = L[j] + L[j-1]
            print('%s' % (L[j]))
            time.sleep(4)
        print('L[i] = %s, L[i-1] = %s' % (L[i],L[i-1]))
        L[i] = 2 * L[i-1]
        

    print(L)
    return L[cube_size - 1]


start = time.time()
n = route_num(20)
elapsed = (time.time() - start)
print("%s found in %s seconds" % (n,elapsed))
