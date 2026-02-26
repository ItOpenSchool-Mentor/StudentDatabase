# Script 4 :: Simple ATM Menu System

balance = 5000

choice = input("Choose Option [balance, withdraw, deposit]")

match choice:
    case "balance":
        print(f"Current Balance is : {balance}")
    case "withdraw":
        amount = int(input("Enter the amount : "))
        if amount <= balance:
            balance -= amount
            print("Withdrawl Successful.....")
            print(f"Remaining Balance : {balance}")
        else:
            print("Warning: Insufficient Funds!")
    case "deposit":
        amount = int(input("Enter the amount : "))
        balance += amount
        print("Deposit Successful.....")
        print(f"Updated Balance : {balance}")
    case _:
        print("Error: Invalid Option.....")

        
