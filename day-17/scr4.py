# Script-2 : Even/Odd + Positive/Negative Checker
# Sol-1: using if..else statement

num = int(input("Enter a number : "))

if num >=0:
    if num % 2 == 0:
        print(f"{num} is +ve Even")
    else:
        print(f"{num} is +ve Odd")
else:
    if num % 2 == 0:
        print(f"{num} is -ve Even")
    else:
        print(f"{num} is -ve Odd")

