# Script-8 : BMI Classifier

height = float(input("Enter Height[m] : "))
weight = float(input("Enter Weight[kg] : "))
bmi = round((weight / height ** 2),1)

if height <= 0 or weight <=0:
    print("Invalid Input")
elif bmi < 18.5:
    print(f"The person with BMI {bmi} is Underweight")
elif bmi <= 24.9:
    print(f"The person with BMI {bmi} is of Normal Weight")
elif bmi <= 29.9:
    print(f"The person with BMI {bmi} is OverWeight")
else:
    print(f"The person with BMI {bmi} is Obese")

    

