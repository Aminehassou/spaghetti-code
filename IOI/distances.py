from math import *
def distance(x1, y1, x2, y2):
    d = sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))
    return d
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
length = distance(x1, y1, x2, y2)
print (length)


