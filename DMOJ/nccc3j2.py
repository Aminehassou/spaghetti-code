found = 0
word = input()
if len(word) == 1:
    print("NO")
else:
    for x in range(1, len(word)):
        half1 = word[0:x]
        half2 = word[x:len(word)]
        if half1[::-1] == half1 and half2[::-1] == half2:
            found = 1
            print("YES")
            break
    if found == 0:
        print("NO")

