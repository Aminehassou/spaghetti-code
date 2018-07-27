n = int(input())
seedDays = list(map(int, input().split()))
days = 0
days += n
for x in range(len(seedDays)):
    if days - (x + 1) < seedDays[x]:
        days = days + ((seedDays[x]) - (days - (x + 1))) 
       
print(days)
