#Define variables by asking user to input 5 numbers
num1 = float(input("Please input a number: "))
num2 = float(input("Please input a number: "))
num3 = float(input("Please input a number: "))
num4 = float(input("Please input a number: "))
num5 = float(input("Please input a number: "))
#Compare num1 to other variables
if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
    #If num1 is greater than or equal to other highest variables, print num1
    print("The highest number is:", num1)
#Compare num2 to other variables
elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
    #If num2 is greater than or equal to other highest variables, print num2
    print("The highest number is:", num2)
#Compare num3 to other variables
elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
    #If num3 is greater than or equal to other highest variables, print num3
    print("The highest number is:", num3)
#Compare num4 to other variables
elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
    #If num4 is greater than other variables, print num4
    print("The highest number is:", num4)
#Compare num5 to other variables
else:
    if num5 >= num1 and num5 >= num2 and num5 >= num3 and num5 >= num4:
         #If num5 is greater than or equal to other highest variables, print num5
         print("The highest number is:", num5)