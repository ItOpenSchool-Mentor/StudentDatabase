
a = int(input("Enter a Value : "))

match a:
    case 1:
        print("One")
    case 2 | 20 | 30:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid Value!")

print("Over.....")
