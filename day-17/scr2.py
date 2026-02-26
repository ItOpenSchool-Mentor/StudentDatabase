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
        match day:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case _:
                print("Sunday")
