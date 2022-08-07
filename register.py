


name = input('enter the name ')
email = input('enter the email')
password = input('enter you password')
confirm = input('enter confirm password ')
gender = input('enter you gender m/f')
if len(name) > 4 and  len(name) < 25:
    if '@'in email:
        if password == confirm :
            print("registration done susscessfully")
        else:
            print(" password does not match")
    else:
        print ("email is invalid")
else:
    print(" name must be between 4 and 25 chars")