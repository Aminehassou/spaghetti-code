nCases = int(input())
for x in range(nCases):
    stringNumber = input()
    while True:
        digits = map(int, list(stringNumber))
        sumDigits = 0
        for digit in digits:
            sumDigits += digit
        if sumDigits < 10:
            print(sumDigits)
            break
        stringNumber = str(sumDigits)
    
    
    