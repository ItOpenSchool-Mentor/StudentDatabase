# Script-3 : Simple Calculator using match statement

num1 = float(input("Enter the Ist Number : "))
num2 = float(input("Enter the IInd Number : "))
operator = input("Enter the Operator[+, -, *, /] : ")

match operator:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Cannot Divide by Zero!")
    case _:
        print("Error: Invalid Operator")

            
