#Euler25
import time

F = [1,1]

while(len(str(F[-1])) < 1000):
      F.append(F[-1] + F[-2])
      
     


print(F.index(F[-1]))
      
      