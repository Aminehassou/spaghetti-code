hauteur = int(input())
nbLeafs = int(input())
treeType = ""
if (hauteur <= 5) and (nbLeafs >= 8):
    treeType = "Tinuviel"
elif (hauteur >= 10) and (nbLeafs >= 10):
    treeType = "Calaelen"
elif (hauteur <= 8) and (nbLeafs <= 5):
    treeType = "Falarion"
else:
    treeType = "Dorthonion"
print(treeType)
