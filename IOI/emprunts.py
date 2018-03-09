values = input().split(" ")
nBooks, nDays = map(int, values)
bookIndexes = [0] * nBooks
for x in range(nDays):
    nClients = int(input())
    for y in range(nClients):
        details = input().split(" ")
        bookIndex, duration = map(int, details)
        if bookIndexes[bookIndex] <= x:  
            print(1)
            bookIndexes[bookIndex] = duration + x
        else:
            print(0)





            

        

