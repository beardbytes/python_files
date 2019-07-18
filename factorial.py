# Program to find a factorial of a number
fact = 1
def fac(n):
    if n==1:
        return fact
    else:
        return (n*(fac(n-1)))

n = int(input("Enter the number: "))
print("The factorial of the number is: ",fac(n))
