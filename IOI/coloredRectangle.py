n = int(input())
for loop in range(n):
    x = int(input())
    y = int(input())
    offPaper = ((x < 0 or y < 0) or (x > 90 or y > 70)) 
    if offPaper:
        print("En dehors de la feuille")
    else:
        isRed = ((x > 15 and x < 45 and y > 60) or (x > 60 and x < 85 and y > 60))
        isYellow = (x < 10 or y < 10 or x > 85 or y > 55 or ((y > 20 and y < 45) and (x > 25 and x < 50)) )
        if isRed:
            print("Dans une zone rouge")
        elif isYellow:
            print("Dans une zone jaune")
        else:
            print("Dans une zone bleue")