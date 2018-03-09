nMonth = int(input())
if (nMonth <= 3) or (nMonth <= 9 and nMonth >= 7):
    print(30)
elif (nMonth <= 6 and nMonth >= 4) or (nMonth == 10):
    print(31)
else:
    print(29)