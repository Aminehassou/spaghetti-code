def isStronger(strg, enStrg, boost):
    if strg > enStrg:
        return boost + strg
    else:
        return 'stop'
s, n = map(int, input().split())
for a in range(n):
    x, y = map(int, input().split())
    s = isStronger(s, x, y)
    if s == 'stop':
        print('NO')
        break
    else:
        print('YES')