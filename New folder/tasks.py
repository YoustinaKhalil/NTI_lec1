# ========== Basic & conditionals ==========

# Check if a number is even or odd
num=int(input("Enter a number "))
if(num%2==0):
    print("Even")
else:
    print("Odd")

# the lastgest number among three numbers
a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=int(input("Enter third number "))
if(a>=b and a>=c):
    print(f"{a} is the largest number")
elif(b>=a and b>=c):
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")

# leap year
year=int(input("Enter a year "))
if(year%4==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Area of circle
r=float(input("Enter radius of circle "))
print(f"Area of circle is {3.14*r*r}")

# positive, negative, zero
num=int(input("Enter a number "))  
if(num>0):
    print("Positive")
elif(num<0):
    print("Negative")
else:
    print("Zero")


# ========== loops ==========

# print numbers from 1 to 10
for i in range(1,11):
    print(i)

# factorial
num=int(input("Enter a number "))
f=1
for i in range(1,num+1):
    f=f*i
print(f"Factorial of {num} is {f}")

# multiplication table
num=int(input("Enter a number "))
for i in range(1,13):
    print(f"{num} * {i} = {num*i}")

# Sum from 1 to n
n = int(input("Enter a number "))
sum = 0
for i in range(1,n+1):
    sum += i
print(f"Sum = {sum}")