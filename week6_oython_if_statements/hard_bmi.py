# BMI Calculator
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height ** 2)
print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
