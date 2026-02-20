
age = int(input("Enter Age : "))

match age:
    case a if a < 18:  # Guard Clause
        print("Minor")
    case a if a >= 18:
        print("Adult")

print("Over.....")    
