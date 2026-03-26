# Implementing Password Functionality
# Module : getpass 
#        Is a Collection Functions 
#        Function : getpass()

from getpass import getpass

correct_pwd = "1234"

for attempts in range(3):
    pwd = getpass("Enter the Password : ")

    if pwd == correct_pwd:
        print("Login Sucessful.....")
        break
    else:
        print(f"Wrong Password ! Attempts Left : {2 - attempts}")
else:
    print("Too many failed attempts, ACCESS BLOCKED!")

