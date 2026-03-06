print("========== SMART COLLEGE ERP SYSTEM ==========")

# Dummy Credentials
student_user = "Arjun"
student_pass = "1234"

admin_user = "admin"
admin_pass = "0000"

#------------LOGIN------------
username = input("Enter UserName : ")
password = input("Enter Password : ")

if username == student_user and password == student_pass:
  role = "student"
elif username == admin_user and password == admin_pass:
  role = "admin"
else:
  role = "invalid"

#---------- DASHBOARD USING match
match role:
  case "student":
    print("Login Successful as STUDENT")
    print("1. Course Selection")
    print("2. Check Result")

    choice = input("Select the Option[1/2] : ")

    #---------- Course Selection ----------
    if choice == "1":
      print("Available Courses:")
      print("1. Python")
      print("2. Data Science")
      print("3. Web Development")

      course_choice = input("Select Course[1/2/3] : ")

      match course_choice:
        case "1":
          course = "Python"
          fee = 20000
        case "2":
          course = "Data Science"
          fee = 40000
        case "3":
          course = "Web Development"
          fee = 30000
        case _:
          course = None
          print("Invalid Course Selection")

      if course:
        print(f"Selected Course : {course}")
        marks = float(input("Enter your 12th Pass Percentage : "))
        income = float(input("Enter Family Annual Income : "))

        # Scholarship Logic
        if marks >= 85 and income <= 300000:
          scholarship = 0.30
        elif marks >= 75:
          scholarship = 0.15
        else:
          scholarship = 0
        discount = fee * scholarship
        final_fee = fee - discount

        print(f"Original fee : {fee}")
        print(f"Scholarship Discount : {discount}")
        print(f"Final Payable Fee : {final_fee}")

    #------ Result Section------
    elif choice == "2":
      score = float(input("Enter Final Exam Marks : "))
      match score:
        case s if s >= 90:
          grade = "A+"
        case s if s >= 75:
          grade = "A"
        case s if s >= 60:
          grade = "B"
        case s if s >= 40:
          grade = "C"
        case _:
          grade = "Fail"
      status = "Passed Successfully" if grade != "Fail" else "Better Luck Time!"

      print(f"Grade = {grade}")
      print(f"Result = {status}")
  # ----------- ADMIN PANEL ----------
  case "admin":    
    print("Login Successful as ADMIN")
    print("1. View System Stats")
    print("2. Fee Structure")

    admin_choice = input("Select Option[1/2] : ")

    if admin_choice == "1":
      print("Total Students Enrolled : 350")
      print("Total Courses Available : 3")
      print("System Status : Running Smoothly")
    elif admin_choice == "2":
      print("Fee Structure")
      print("1. Python : Rs 20,000")
      print("2. Data Science : Rs 40,000")
      print("3. Web Development : Rs 30,000")
    else:
      print("Invalid ADMIN Option")

  # -------Invalid Login ----------
  case _:
    print("Invalid Login Credentials!") 
    
