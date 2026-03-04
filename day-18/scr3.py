print("========== Food Ordering System =========")
item = input("Enter Item(pizza/burger/pasta) : ").lower()
quantity = int(input("Enter the Quantity : "))
# Price Mapping
match item:
  case "pizza":
    price = 250
  case "burger":
    price = 120
  case "pasta":
    price = 180
  case _:
    print("Invalid Item Selected!")
    price = 0
if price > 0:
  total = price * quantity
  # discount calc
  if total >= 1000:
    discount = total * 0.10
  elif total >= 500:
    discount = total * 0.05
  else:
    discount = 0
  final_amount = total - discount
  tax = final_amount * 0.05
  payable = final_amount + tax
  print(f"Total : {total}")
  print(f"Discount : {discount}")
  print(f"GST : {tax}")
  print(f"Final Payable Amount : \u20B9 {payable}")





