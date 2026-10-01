# c = 20
# print(f"Celsius = {c}")
# f = (c*9/5)+32
# print(f"Fahrenheit = {f}")


num=int(input("Enter a number "))

if (num>=1 and num<=10):
    if(num%2==0):
        print("Even")
    else:
        print("Odd")
else :
    print ("Number is not between 1 and 10")