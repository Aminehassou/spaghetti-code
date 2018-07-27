from math import *
n, m, a = map(int, input().split())
flagstones = 0
flagstones = ceil(n / a) * ceil(m / a)
print(flagstones)