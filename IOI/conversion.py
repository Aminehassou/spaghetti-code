n = int(input())
for x in range(n):
   value = str(input())
   v = value.split(" ")
   num = float(v[0])
   for y in v:
       if y == "m":
           print(num/0.3048, "p")
       if y == "g":
           print(num*0.002205, "l")
       elif y == "c":
           print((num*1.8)+32, "f") 
    
        
