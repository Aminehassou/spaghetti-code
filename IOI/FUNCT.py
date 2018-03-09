def exes(number):
    for x in range(number):
        print("X", end = "")
    print()
def hashes(lines, columns):
    for y in range(lines):
        if not y == 0:
           print()
        for x in range(columns):
            if y == 0 or y == lines-1:
               print("#", end = "")
               
            else:
               if x == 0 or x == columns-1:
                  print("#", end = "")
               else:
                  print(" ", end = "")
    print()
def signs(lines):
   for x in range(1, lines+1):
      if x == 1 or x == lines:
         print("@"*x)
      else:
         print("@", end = " "*(x-2))
         print("@")
xLines = int(input())
hashLines = int(input())
hashCols = int(input())
atLines = int(input())
def main():   
   exes(xLines)
   print()
   hashes(hashLines, hashCols)
   print()
   signs(atLines)
main()
            