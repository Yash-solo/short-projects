string = input("Enter your password")
if any(char in string for char in "!!@##$%^&*()"):
    if any(num in string for num in "1234567890"):
        if len(string)>8:
            print("Strong password")
        else:
            print("medium-strongpassword")
    elif len(string)>8:
        print("Medium password")
    else:
        print("Medium password")
else:
    print("Your password is weak")        
