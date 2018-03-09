missingNumber = int(input())
nList = int(input())
result = "Encore dans la ville"
for x in range(nList):
    number = int(input())
    found = (number == missingNumber)
    if found:
        result = "Sorti de la ville"
print (result)