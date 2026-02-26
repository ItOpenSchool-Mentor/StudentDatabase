# Script - 1: Day of Week Detector

day_input = input("Enter the Day Number[1-7] : ")

# Validation: Ensure Numeric Input
if not day_input.isdigit():
    print("Error: Invalid Value!")
else:
    day = int(day_input)
    # Range Validation
    if day < 1 or day > 7:
        print("Error: Day number must be between 1 and 7")
    else:
        if day == 1:
            print("Monday")
        elif day == 2:
            print("Tuesday")
        elif day == 3:
            print("Wednesday")
        elif day == 4:
            print("Thursday")
        elif day == 5:
            print("Friday")
        elif day == 6:
            print("Saturday")
        else:
            print("Sunday")
