from re import findall
from math import sqrt
def isPrime(number):
    if number == 2 or number == 3:
        return  True
    if number % 2 == 0 or number < 2 :
        return False
    tester = int(sqrt(number)) + 1
    for divisor in range(3, tester, 2):
        if number % divisor == 0:
            return False
    return True

n = int(input())
stringN = str(n)
if len(stringN) == 1:
    print(1)
else:
    answer = 0
    flag = 0
    for splitter in range(1, len(stringN) + 1):
        digits = findall('.?'*splitter, stringN)
        for element in digits:
            if element != "":
                if isPrime(int(element)) == False:
                    flag = 1
        if flag == 0:               
            answer = len(digits) - 1
        print(answer)


