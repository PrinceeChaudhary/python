num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
operate = input("Enter the operation")
if (operate == "+"):
    calculation = num1 + num2
elif (operate == "-"):
    calculation = num1 - num2
elif (operate == "*"):
    calculation = num1 * num2
else:
    calculation = num1 / num2


print (f"your result is{calculation}")
