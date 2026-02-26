# Script-2 : Even/Odd + Positive/Negative Checker
# Sol-2: using Ternary Operator/Conditional Expression

num = int(input("Enter a number : "))

parity = "Even" if num % 2 == 0 else "Odd"

sign = "+ve" if num >= 0 else "-ve"

print(f"{num} is {sign} {parity}")

