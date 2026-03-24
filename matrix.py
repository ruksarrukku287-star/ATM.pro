Array=[1,2,3,4]
r=int(input("enetr row size"))
c=int(input("enter column size"))
L=[]
for i in range (0,r,1):
    L.append([])
    for j in range(0,c,1):    
        val=int(input(f"enter element [{i}][{j}]:"))
        L[i].append(val)
print("matrix is:")
for i in range(r):
    print(L[i])
