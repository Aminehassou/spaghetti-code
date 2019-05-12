t = int(input())
for x in range(t):
    used = []
    count = 0 
    n = int(input())
    colors = list(map(int, input().split()))
    for y in range(len(colors)):
        if colors[y] != 0:
            count+=1
    print(count)        
       
    

    