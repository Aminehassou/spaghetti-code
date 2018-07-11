nFriandises = int(input())
p1 = ""
p2 = ""
letter = list(input())
points = 0
print(len(letter))
for x in range(len(letter)):
    if x == 0:
        p1 += letter[x]
        points += 1
    elif x == 1:
        if letter[x] != p1[-1]:
            p1 += letter[x]
            points += 1
        elif letter[x] != p2[-1]:
            p2 += letter[x]
            points += 1
        elif letter[x] == p1[-1]:
            p1 += letter[x]
            points += 1
        elif letter[x] == p2[-1]:
            p2 += letter[x]
            points += 1
    else:    
        
        if letter[x] != p1[-1] and p1[-1] != p1[-2]:
            p1 += letter[x]
            points += 3
        elif letter[x] != p2[-1] and p2[-1] != p2[-2]:
            p2 += letter[x]
            points += 3
        elif (letter[x] == p1[-1] and p1[-1] != p1[-2]) or (letter[x] != p1[-1] and p1[-1] == p1[-2]):
            p1 += letter[x]
            points += 2
        elif (letter[x] == p2[-1] and p2[-1] != p2[-2]) or (letter[x] != p2[-1] and p2[-1] == p2[-2]):
            p2 += letter[x]
            points += 2
        elif (letter[x] == p1[-1] and p1[-1] == p1[-2]):
            p1 += letter[x]
            points += 1
        elif (letter[x] == p2[-1] and p2[-1] == p2[-2]):
            p2 += letter[x]
            points += 1
    print("p1:", p1)
    print("p2:", p2)
print(points)


        



