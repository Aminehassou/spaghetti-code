n = int(input())
def average(list, c):
    average = 0
    averages = []
    for x in range(len(list)):
        for y in range(1, len(list[x])):
            average += list[x][y]
        average = average / list[x][0]
        averages.append(average)
        return(averages[c])

for x in range(n):
    above = 0
    points = []
    N = list(map(int, input().split()))
    points.append(N)
    for y in range(len(points)):
        for z in range(len(points[y])):
            if points[x][y] >= average(points, x):
                above += 1
                print(above) 

    


