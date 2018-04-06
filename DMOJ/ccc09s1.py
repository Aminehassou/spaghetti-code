from math import *
a = int(input())
b = int(input())
count = 0
for number in range(floor(sqrt(a)), ceil(sqrt(b))+1):
    n = number**2
    for x in range(floor(a**(1/3)), ceil(b**(1/3))+1):
        m = x**3
        if m > n:
            break
        if n == m:
            count+=1
            break 
print(count)


