from math import *
oldTax = float(input())
newTax = float(input())
price = float(input())
oldPrice = price / (1 + oldTax/100)
#price = oldPrice + oldPrice * oldTax / 100
tax = (oldPrice * newTax) / 100
newPrice = oldPrice + tax
print(round(newPrice*100) / 100)