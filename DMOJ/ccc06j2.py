m = int(input())
n = int(input())
counter = 0
for x in range(1, m + 1):
    for y in range(n, 0, -1):
        if y + x == 10:
            counter+=1
group = "way"
isAre = "is"
if counter > 1 or counter == 0:
    group = "ways"
    isAre = "are"
print("There {} {} {} to get the sum 10.".format(isAre, counter, group))