title = input()
author = input()
for x in title:
    if not (x == "A" or x == "E" or x == "I" or x == "O" or x == "U" or x == " "):
        print(x, end ="")
print()        
for x in author:
    if not (x == "A" or x == "E" or x == "I" or x == "O" or x == "U" or x == " "):
        print(x, end ="")

        