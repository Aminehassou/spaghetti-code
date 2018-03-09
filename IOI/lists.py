'''
5 2 1
3 10 5
2 0 8
'''
sqr = [5, 2, 1, 3, 10, 5, 2, 0, 8, 9, 7, 3]
for x in range(0, len(sqr)):
    if x%3==0 and x!=0:
        print()
    print(sqr[x], end = " ")
    

