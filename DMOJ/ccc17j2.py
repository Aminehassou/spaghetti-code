number = int(input())
nShifts = int(input())
orgNumber = number
for x in range(nShifts):
    number = number + (orgNumber*10)
    orgNumber = orgNumber*10
print(number)