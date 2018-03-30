happy =":-)"
sad =":-("
phrase = input()
happies = phrase.count(happy)
sads = phrase.count(sad)
if happies > sads:
    print("happy") 
elif happies < sads:
    print("sad")
elif happies == sads and happies>0 and sads>0:
    print("unsure")
else:
    print("none")