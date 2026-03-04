print("========== University Admission System ==========")

stream = input("Enter desired Stream(science/commerce/arts) : ").lower()
percentage = float(input("Enter 12th Class Percentage : "))

match stream:
  case "science":
    if percentage >= 85:
      print("Admission Confirmed in Science Stream")
    elif percentage >= 75:
      print("You are on the Science Stream Waiting List")
    else:
      print("Not Eligible for Science Stream")
  case "commerce":
    if percentage >= 70:
      print("Admission Confirmed in Commerce Stream")
    else:
      print("Not Eligible for Commerce Stream")
  case "arts":
    if percentage >= 50:
      print("Admission Confirmed in Arts Stream")
    else:
      print("Not Eligible for Arts Stream")
  case _:
    print("Invalid Stream Selected")




