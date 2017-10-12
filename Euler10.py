import time

def isprime(n):

    if n == 1:
        return False
    elif n<4:
        return True
    elif n%2 == 0:
        return False
    elif n<9:
        return True
    elif n%3 == 0:
        return False

    i = 5
    
    while(i*i <= n):
        if n%i == 0:
            return False
        elif n%(i+2) == 0:
            return False
        i += 6

    return True



def nprimesum(n):

    Sum = 2
    count = 1
    contestant = 3

    while(contestant <= n):

        if isprime(contestant):
            Sum += contestant
            contestant += 2

        else:
            contestant += 2

##        print(contestant)
        

    return Sum



start = time.time()
Sum = nprimesum(2000000)
end = time.time()

print('The sum is %s and it took %s seconds' % (Sum,end-start))
