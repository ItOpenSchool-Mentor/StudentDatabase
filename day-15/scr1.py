##You are eligible to vote age >= 18
##You are NOT eligible to vote age < 18

msg = "You are NOT eligible to vote"

age = int(input("Enter your Age : "))

if age >= 18:
    msg = msg.replace("NOT ", "")

print(msg)

