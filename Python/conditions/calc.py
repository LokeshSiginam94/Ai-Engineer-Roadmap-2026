num1=int(input("Enter the first number:"))
operator=input("Select the operator:+,-,/,%,*,**")
num2=int(input("Enter the second number:"))


if operator=="+":
    print("The sum of two numbers is:",num1+num2)
elif operator=="-":
    print("The diff of two numbers is:",num1-num2)
elif operator=="/":
    print("The div of two numbers is:",num1/num2)
elif operator=="*":
    print("The mul of two numbers is:",num1*num2)
elif operator=="**":
    print("The power of two numbers is",num1**num2)
elif operator=="%":
    print("The modulo of two numbers is",num1%num2)
else:
    print("Invalid!")    

        

