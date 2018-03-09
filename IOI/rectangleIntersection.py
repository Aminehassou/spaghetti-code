'''
rect 2
0 3 0 3
rect 1
4 5 4 5
'''
nbPairs = int(input())
for x in range(nbPairs):
    rect1_xmin = int(input())
    rect1_xmax = int(input())
    rect1_ymin = int(input())
    rect1_ymax = int(input())
    rect2_xmin = int(input())
    rect2_xmax = int(input())
    rect2_ymin = int(input())
    rect2_ymax = int(input())
    if (rect1_xmin >= rect2_xmax) or (rect2_xmin >= rect1_xmax) or (rect1_ymin >= rect2_ymax) or (rect2_ymin >= rect1_ymax):
        print("NON")
    else:
        print("OUI")