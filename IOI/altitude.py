totalClimb = 0
totalDescent = 0
n = int(input())
for x in range(n):
    altitude = int(input())
    if altitude > 0:
        totalClimb += altitude
    else:
        totalDescent -= altitude
print (totalClimb)
print (totalDescent)
