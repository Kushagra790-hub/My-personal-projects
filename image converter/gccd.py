a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if (a>b):
    for i in range(1,a):
        if(a % i == 0 and b % i == 0):
            c = i 
else:
    for i in range(1,b):
        if(a % i == 0 and b % i == 0):
            c = i


print("The Greatest Common Divisor(GCD) is: ",c)