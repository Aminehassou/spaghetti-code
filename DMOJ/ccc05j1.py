def planA(minutesDay, minutesEve, minutesEnd):
    paidMinutes = minutesDay - 100
    if paidMinutes < 0:
        paidMinutes = 0
    priceA = ((paidMinutes*25) + (minutesEve*15) + (minutesEnd*20))/100
    return priceA
def planB(minutesDay, minutesEve, minutesEnd):
    paidMinutes = minutesDay - 250
    if paidMinutes < 0:
        paidMinutes = 0
    priceB = ((paidMinutes*45) + (minutesEve*35) + (minutesEnd*25))/100
    return priceB

mins = []
for x in range(3):
    mins.append(int(input()))
planA = planA(mins[0], mins[1], mins[2])
planB = planB(mins[0], mins[1], mins[2])
print("Plan A costs", planA)
print("Plan B costs", planB)
if planA < planB:
    print("Plan A is cheapest.")
elif planB < planA:
    print("Plan B is cheapest.")
else:
    print("Plan A and B are the same price.")