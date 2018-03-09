length = int(input())
def dentelle(symbol, length):
    for x in range(length):
        print(symbol, end = "")
    print()
dentelle("X", length)
dentelle("#", length)
dentelle("i", length)