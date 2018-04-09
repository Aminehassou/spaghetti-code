n = int(input())
count = 0
tries = []
answers = []
for guess in range(n):
    tries.append(input())
for answer in range(n):
    answers.append(input())
for index in range(len(tries)):
    if tries[index] == answers[index]:
        count+=1    
print(count)