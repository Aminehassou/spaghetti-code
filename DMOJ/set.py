import sys
unique=sys.stdin.read().split("\n")
st=set()
for x in range(1,int(unique[0])+1):
    if unique[x] not in st:
        st.add(unique[x])
print(len(st))
