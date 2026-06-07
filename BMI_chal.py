import time
print("========BMI Chalculator========")
weight = int(input("Enter your weight in kg:"))
height = float(input("Enter your height: (foot.inches):-"))

#BMI chalculations

height_in_m2 = (((int(height)*12)+round((height-int(height))*10,3))*0.0254)**2
Bmi = round(weight/height_in_m2,2)
print("\nBMI:-",Bmi)

#conditions
if Bmi<18.0:
    print("Underweight")
elif Bmi>=18.0 and Bmi<=24.9:
    print("Healthy Weight")
elif Bmi>25.0 and Bmi<=29.9:
    print("Overweight")
elif Bmi>=30.0:
    print("Obese")
else:
    None

print("\nProgram is closing.....")
time.sleep(3)
print("Program closed successfully")