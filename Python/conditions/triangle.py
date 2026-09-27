side1=int(input("Enter the side1:"))
side2=int(input("Enter the side2:"))
side3=int(input("Enter the side3:"))

#all individual
# if side1+side2>side3:
#     print("Valid")
# elif side2+side3>side1:
#     print("Valid")
# elif side1+side3>side2:
#     print("Valid")        
# else:
#     print("Not Valid!")

# all in one
if side1+side2>side3 and side2+side3>side1 and side3+side1>side2:
    print("Valid!")
else:
    print("Not Valid!")    

if side1==side2==side3:
    print("Equilateral")
elif side1==side2 or side2==side3 or side3==1:
    print("Isosceles")
else:
    print("Scalene")
