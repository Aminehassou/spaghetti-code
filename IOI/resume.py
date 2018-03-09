nBooks = int(input())
lMin = int(input())
for x in range(nBooks):
    title = str(input())
    resume = str(input())
    if len(resume) < lMin:
        print(title) 