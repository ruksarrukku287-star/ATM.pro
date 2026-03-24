n=int(input("enter number"))
c=0
for i in range(1,n+1,1):
    if(n%i==0):
        c+=1
if(c==2):
    print("n is prime")
else:
    print("n is not prime") 
