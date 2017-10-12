import math

def PTGC(a,b):

    return math.sqrt((a*a) + (b*b))


A = []
B = []
C = []

i = 0





for a in range(0,1001):
    for b in range(a+1,1001):
        c = PTGC(a,b)
        if (a<b<c) and (a+b+c ==1000):
            print(a*b*c)
        else:
            continue
            
        
##for c in reversed(range(0,1001)):
##
##    Next = False
##
##    print('c is %s' % (c))
##
##    for b in reversed(range(0,1001)):
##
##        print('b is %s' % (b))        
##
##        if (c + b) > 1000:
##            break        
##
##        for a in reversed(range(0,1001)):
##            print('a is %s' % (a))
##            
##            if (b + a) > 1000:
##                break
##            
##            elif ((a+b+c) == 1000) and (a<b<c):
##                A.append(a)
##                B.append(b)
##                C.append(c)
##                i += 1
##                print(i)
            
                

print(A)
print(B)
print(C)

    
