burgerCal = [0, 461, 431, 420, 0]
sideCal = [0, 100, 75, 70, 0]
drinkCal = [0, 130, 160, 118, 0]
dessertCal = [0, 167, 266, 75, 0]
totalCals = 0
totalCals += burgerCal[int(input())]
totalCals += sideCal[int(input())]
totalCals += drinkCal[int(input())]
totalCals += dessertCal[int(input())]
print("Your total Calorie count is {}.".format(totalCals))