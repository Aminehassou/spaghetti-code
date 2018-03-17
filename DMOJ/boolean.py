booleanString = input().split(" ")
if booleanString.count("not") % 2 == 0:
    print(booleanString[-1])
elif booleanString.count("not") % 2 == 1:
    if booleanString[-1] == "True":
        print("False")
    else:
        print("True")