from math import *
def isPrime(number):
    if number == 1:
        return False
    for x in range(2, floor(sqrt(number)) + 1):
        if number % x == 0:
            return False
    return True
number = int(input())
while not isPrime(number):
    number+=1
print(number)


  