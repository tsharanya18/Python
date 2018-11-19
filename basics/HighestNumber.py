num1 = input("Enter a number : ")
num2 = input("Enter a number : ")
num3 = input("Enter a number : ")

if num1 >= num2 and num1 >= num3:
    print("Highest Number is " + num1)
elif num2 >= num3 and num2 >= num1:
    print("Highest Number is " + num2)
else:
    print("Highest Number is " + num3)
