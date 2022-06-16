
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
print("what do you want to do?"+"+,-,*,/")
num3 =input()
    

if num1 == 4 and num2 == 5 and num3 == '*':
    print("15")
elif num1 == 15 and num2 == 20 and num3 == "+":
    print("40")
elif num1 == 10 and num2 == 5 and num3 == "-":
    print("2")
elif num1 == 10 and num2 == 5 and num3 == "-":
    print("3")

elif num3 ==  "*":
    multiply = num1*num2
    print("=",multiply)
elif num3 ==  "+":
    addition = num1+num2
    print("=",addition)
elif num3 ==  "-":
    subtraction = num1-num2
    print("=",subtraction)
elif num3 ==  "/":
    division = num1/num2
    print("=",division)
else:
        print("out of range")

  