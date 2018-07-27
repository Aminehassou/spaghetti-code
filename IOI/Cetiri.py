a, b, c = map(int, input().split())
values = sorted([a, b, c])
diff = values[2] - values[1]
diff2 = values[1] - values[0]
if diff == diff2:
    print(diff + values[2])
elif diff != diff2:
    if diff > diff2:
        print(values[1] + diff2)
    if diff < diff2:
        print(values[0] + diff)

    