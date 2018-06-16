def isLanguage(tTcount, sScount):
    if t_TCount > s_SCount:
        return "English"
    if t_TCount < s_SCount:
        return "French"
    return "French"
n = int(input())
t_TCount = 0
s_SCount = 0 
for x in range(n):
    line = input()
    t_TCount += line.count("t")
    t_TCount += line.count("T")
    s_SCount += line.count("s")
    s_SCount += line.count("S")
print(isLanguage(t_TCount, s_SCount))
