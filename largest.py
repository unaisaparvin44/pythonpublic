num1=int(input("enter your first number:"))
num2=int(input("enter your 2nd number"))
num3=int(input("enter your 3rd number"))
if num1>=num2 and num1>=num3:
    largest=num2
else:
    largest=num3
    print("the largest number is:",largest)
