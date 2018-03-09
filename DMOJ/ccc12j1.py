speedLimit = int(input())
carSpeed = int(input())
overLimit = carSpeed - speedLimit
if overLimit <= 20 and overLimit >= 1:
    print("You are speeding and your fine is $", end="")
    print(100,  end = "")
    print(".")

elif overLimit <= 30 and overLimit >= 21:
    print("You are speeding and your fine is $", end="")
    print(270, end = "")
    print(".")
elif overLimit >= 31:
    print("You are speeding and your fine is $", end="")
    print(500, end = "")
    print(".")

else:
    print("Congratulations, you are within the speed limit!")