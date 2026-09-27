char=input("Enter one character:")

if char.isalpha():
    if char in "aeiouAEIOU":
        print("Vowel")
    else:
        print("Consonent")

if char.isdigit():
   print("Digit")
else:
    print("Special Character:")          
        
