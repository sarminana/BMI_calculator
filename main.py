# BMI Calculator (imperial units)
name = input("What is your name? ")

height_inches = float(input("How tall are you? (in inches) "))

weight_lbs = float(input("How much do you weigh? (in lbs) "))

BMI = float(weight_lbs * 703) / (height_inches ** 2)

# round(BMI,1) will round to nearest tenth place
print(f"{name}, your BMI is", round(BMI, 1))

# Cancer Organization BMI Classification -> https://www.cancer.org/cancer/cancer-causes/diet-physical-activity/body-weight-and-cancer-risk/adult-bmi.html
if BMI < 18.5:
    print(name, "is underweight")
elif 18.5 < BMI < 24.9:
    print(name, "is normal weight")
elif 25 < BMI < 29.9:
    print(name, "overweight")
elif BMI > 30:
    print(name, "is obese")
