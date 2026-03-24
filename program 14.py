def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter number:"))
print("Factorial of", n, "is", fact(n))
