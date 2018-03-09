
s = input().split(" ")
nlines, nwords = map(int, s)
lengths = [0] * 101
for x in range(nlines):
    line = input()
    words = line.split(" ")
    for w in words:
        lengths[len(w)] += 1
for x in range(101):
    if lengths[x] > 0:
        print("{} : {}".format(x, lengths[x]))





