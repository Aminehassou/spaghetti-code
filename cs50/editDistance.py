from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())
print(Operation.DELETED.value)
def editDistance(s, r):
    rows = len(s)
    cols = len(r)
    d = [[(-1,)] * (cols + 1) for i in range(rows+1)]
    for i in range(cols + 1):
        d[0][i] = (i, Operation.INSERTED)
    for i in range(rows + 1):
        d[i][0] = (i, Operation.DELETED)
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            cost = -1
            op = None
            temp = d[i-1][j-1][0]
            if s[i-1] != r[j-1]:
                temp += Operation.SUBSTITUTED.value
            insertCost = d[i-1][j][0] + Operation.INSERTED.value
            deleteCost = d[i][j-1][0] + Operation.DELETED.value  
            cost = min(insertCost, deleteCost, temp)
            if cost == insertCost:
                op = Operation.INSERTED
            elif cost == deleteCost:
                op = Operation.DELETED
            else:
                op = Operation.SUBSTITUTED
            d[i][j] = (cost, op)
    print(d)
    return d[rows][cols]
print(editDistance("intention", "execution"))