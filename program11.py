
a=5
b=6
c=2
s=a+b+c
print("sum of 3numbers",s)


a=5
b="5"
c=4.0
print(type(a))
print(type(b))
print(id(a))

numbers=[10,5,8,20,18]
unique_numbers=list(set(numbers))
unique_numbers.sort()
second_largest=unique_numbers[-2]
print("second largest number",second_largest)


l=list(map(int,input("enter").split()))
print(l)
l=list(set(l))
l.sort()
print(l[-2])

n=int(input("enter number"))
c=0
for i in range(1,n+1,1):
    if(n%i==0):
        c+=1
if(c==2):
    print("n is prime")
else:
    print("n is not prime") 
