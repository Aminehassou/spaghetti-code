n, k = map(int, input().split(" "))
points = n
flag = 0
s = list(map(int, input().split(" ")))
y = 0
for y in range(len(s)-1):
    if s[y+1] != s[y] + k:
        print("y = ", y)
        flag = 1
        points -= 1
    print(points)
