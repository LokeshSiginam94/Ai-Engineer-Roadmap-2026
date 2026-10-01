num1=input("Enter the first number: ")
operator=input("Enter the operator(+,-,/,*,//,**,%): ")
num2=input("Enter the second number: ")

if operator=="+":
    print("The sum of the two numbers is:",int(num1)+int(num2))
elif operator=="-":
    print("The difference of the two numbers is:",int(num1)-int(num2))
elif operator=="/":
    print("The quotient of the two numbers is:",int(num1)/int(num2))
elif operator=="*":
    print("The product of the two numbers is:",int(num1)*int(num2))
elif operator=="//":
    print("The floor quotient of the two numbers is:",int(num1)//int(num2))
elif operator=="**":
    print("The power of the two numbers is:",int(num1)**int(num2))
elif operator=="%":
    print("The remainder of the two numbers is:",int(num1)%int(num2))
else:
    print("Invalid operator")
