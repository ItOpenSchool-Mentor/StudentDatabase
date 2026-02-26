# Script-7 : Leap Year Checker

year = int(input("Enter the Year : "))

if year <= 0:
    print("Error: Invalid Year Value[must be > 0]")
elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Year {year} is a Leap Year")
else:
    print(f"Year {year} is NOT a Leap Year")
