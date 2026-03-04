print("Scholarship Eligibility System")

name = input("Enter Student's Name : ")
marks = float(input("Enter Percentage : "))
family_income = float(input("Enter family's Annual Income : ")) 

if marks < 0 or marks > 100:
  print("Invalid Marks Entered!")
else:
  if marks >= 85 and family_income  <= 300000:
    print(f"Student {name} is Eligible for Full Scholarship")
  elif marks >= 75 and family_income <= 500000:
    print(f"Student {name} is Eligible for Partial Scholarship")
  elif marks >= 60:
    status = "Eligible for Merit Certificate" if family_income > 500000 else "Needs Review!"
    print(f"{name} : {status}")
  else:
      print(f"{name} is NOT Eligible for Scholarship")


