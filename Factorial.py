def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
i=int(input("Please enter the number whose factorial you want"))
print("the factorial of ",i,"is",factorial(i))