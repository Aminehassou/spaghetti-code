import sys
nVotes = int(sys.stdin.readline())
characters = sys.stdin.readline().rstrip()
A = 0
B = 0
for x in characters:
    if x == "A":
        A += 1
    elif x == "B":
        B += 1
if A > B:
    print("A")
elif B > A:
    print("B")
else:
    print("Tie")
