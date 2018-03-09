debut1 = int(input())
fin1 = int(input())
debut2 = int(input())
fin2 = int(input())
minDebut = 0
if debut1 <= debut2:
    minDebut = debut1
else:
    minDebut = debut2
if (fin1 >= debut2 and minDebut == debut1) or (fin2 >= debut1 and minDebut == debut2):
    print ("Amis")
else:
    print ("Pas amis")