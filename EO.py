l=[3,2,4,5,6,7,9]
for i in l:
    if(i%2==0):
        print("even number:",i) 
    else:
        for j in range(2,i):
            if i%j==0:
                print("odd number:",i)
                break
        else:
            print("prime number:",i)





n=int(input("enter number"))
c=0
print("divisiblities of given number")




            
