lines = int(input())
columns = int(input())
value = input()
def dentelle(lines, columns, value):
    for x in range(lines):
        for y in range(columns):
            print(value, end = "")
        print()
    
dentelle(lines, columns, value)
