height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight/height ** 2)

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are \033[1munderweight.")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you have a \033[1mnormal weight.")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are \033[1mslightly overweight.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are \033[1mobese.")
else:
    print(f"Your BMI is {bmi} you are \033[1mclinically obese.")
