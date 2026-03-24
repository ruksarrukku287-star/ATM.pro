n=int(input("enter number"))
if(n==0):
    print("factorial 0 is 1")
else:
    p=1
    for i in range(1,n+1,1):
        p=p*i
        print(p)
