costMin = 40
costAvg = 50
costMax = 60
duration = int(input("Enter Duration "))
gamesWon = int(input("Enter Games Won Per Day "))
matchGold = (gamesWon//3)*10
if gamesWon >= 30:
	matchGold=100
totalGoldMin = (costMin + matchGold) * duration
totalGoldAvg = (costAvg + matchGold) * duration
totalGoldMax = (costMax + matchGold) * duration
print ("(Minimum)", "You can make", totalGoldMin, "gold in", duration, "days")
print ("(Average)", "You can make", totalGoldAvg, "gold in", duration, "days")
print ("(Maximum)", "You can make", totalGoldMax, "gold in", duration, "days")