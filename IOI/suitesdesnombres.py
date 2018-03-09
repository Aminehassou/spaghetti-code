def next(v):
    if v % 2 == 0:
        return v // 2
    else:
        return (v*3) + 1
number = int(input())
while number != 1:
    number = next(number)
    print(number, end = " ")
