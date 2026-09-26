number=int(input("Enter the number:"))

if number<0:
    print("Negative")
elif number>0:
    print("Positive")
else:
    print("Zero")

if number %2 == 0:
    print("Even") 
else:
    print("Odd")           