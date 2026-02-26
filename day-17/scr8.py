# Script 5 : Grade System Using match with Guard

marks = int(input("Enter Marks : "))

match marks:
    case m if m >= 90:
        print("Grade-A+")
    case m if m >= 75:
        print("Grade-A")
    case m if m >= 60:
        print("Grade-B")
    case m if m >= 40:
        print("Grade-C")
    case _:
        print("Fail.....")



        
