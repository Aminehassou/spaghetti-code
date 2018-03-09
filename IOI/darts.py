nLetters = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
length = nLetters * 2 - 1
row = "a" * length
rows = []
for x in range(1, nLetters + 1):
    print(row)
    rows.append(row)
    if x <= nLetters:
        for filler in range(x, len(row) - x):
            eRow = list(row)
            for y in range(x, len(eRow) - x):
                eRow[y] = alphabet[x]
            row = "".join(eRow)
    
for x in range(len(rows) - 2, -1, -1):
    print(rows[x])

