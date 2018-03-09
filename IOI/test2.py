
l1 = [5, 3, 9, -2, -7]
l2 = [1, 8, 2, -9, -4]
def add(a, b):
    return a+b

def squareSum(a, b):
    res = add(a, b)
    return res * res

for x in range(len(l1)):
    print (squareSum(l1[x], l2[x]))
    