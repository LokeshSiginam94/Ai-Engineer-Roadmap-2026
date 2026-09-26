year=int(input("Enter the Year:"))

if (year%4 == 0) and (year%100 !=0 or year%400 ==0):
    print("You entered a leap year")
else:
    print("Not a leap year")