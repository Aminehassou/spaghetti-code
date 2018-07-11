
def c_compatible(variable):
    x = 0
    upLow_ = (("a" <= variable[x] and variable[x] <= "z") or ("A" <= variable[x] and variable[x] <= "Z")) or variable[x] == "_"
    if not upLow_:
        return "NO"
    for y in range(1, len(variable)):
        c = variable[y]
        if not ((("a" <= c and c <= "z") or ("A" <= c and c <= "Z")) or c == "_" or c.isdigit()):
            return "NO"
    return "YES"

n = int(input())
for x in range(n):
    variable = input()
    print(c_compatible(variable))