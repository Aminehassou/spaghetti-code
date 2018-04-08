yearX = int(input())
yearY = int(input())
for year in range(yearX, yearY+1):
    yearDiff = year - yearX 
    if yearDiff % 4 == 0 and yearDiff % 2 == 0 and yearDiff % 3 == 0 and yearDiff % 5 == 0:
        print("All positions change in year", year)
