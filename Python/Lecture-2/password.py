password = input("Enter the password: ")

has_digit = False

for ch in password:
    if ch.isdigit():
        has_digit = True

if len(password) >= 8 and has_digit and " " not in password:
    print("Strong Password!")
else:
    print("Not a Strong Password")