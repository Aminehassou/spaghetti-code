import sys
from random import randint
sys.stdin = open('a2.in', 'r')
sys.stdout = open('a2.out', 'w')

def getPower_10(number):
    if number == 100:
        return number
    elif number >= 10:
        return 10
    else:
        return 1

#n = number of wheels
#The i-th wheel from the left contains the integers from 1 to ki
#The integers are randomly chosen
cases = int(input())
for x in range(cases):
    input()
    n = input()
    elements = input().split(" ")
    for y in range(len(elements)):
        elements[y] = getPower_10(int(elements[y]))
    elements[-1] = 1
    print(" ".join(map(str, elements)))
        
    