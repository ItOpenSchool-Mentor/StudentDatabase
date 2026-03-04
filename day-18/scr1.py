print("========== Welcome to ABC Bank ==========")

account_number = input("Enter the Account Number : ")
pin = input("Enter 4-Digit PIN : ")

# Stored Dummy Credentials
stored_account_no= "123456789"
stored_pin = "4321"
balance = 15000

if account_number == stored_account_no:
  if pin == stored_pin:
    print("Login Successful.....\n")
    print("Menu Options:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    choice = input("Select Option[1/2/3] : ")

    if choice == "1":
      # Displaying the Balance
      print(f"Available Balance : {balance}")
    elif choice == "2":
      # Withdraw Amount
      amount = float(input("Enter Withdrawl Amount : "))
      if amount > 0 and amount <= balance:
        balance -= amount
        print("Withdrawl Successful")
        print(f"Remaining Balance : {balance}")
      else:
        print("Invalid or Insufficient Balance!")
    elif choice == "3":
      # Deposit Amount
      amount = float(input("Enter Deposit Amount : "))
      if amount > 0:
        balance += amount
        print("Deposit Successful")
        print(f"Updated Balance : {balance}")
      else:
        print("Invalid Deposit Amount")
    else:
      print("Invalid Menu Choice!")
  else:
    print("Invalid PIN!")     
else:
  print("Invalid Account Number!") 
 



