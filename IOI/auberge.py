age = int(input())
poids = int(input())
cost = 0
if age == 60:
    cost = 0
elif age < 10:
    cost = 5
else:
    cost = 30
    if poids >= 20:
        cost += 10
print(cost)