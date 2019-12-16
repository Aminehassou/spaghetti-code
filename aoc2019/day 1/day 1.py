# --- Day 1: The Tyranny of the Rocket Equation --- #

from math import floor
def calculateFuel(mass):
    fuel = floor(int(mass) / 3) - 2
    return fuel

inputFile = open("input.txt", "r")
add = 0
for line in inputFile:
    fuel = calculateFuel(line)
    add += fuel
    while calculateFuel(fuel) > 0:
        fuel = calculateFuel(fuel)
        add += fuel
    print(add)

    
