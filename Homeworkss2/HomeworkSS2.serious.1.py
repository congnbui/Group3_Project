print("Calculate your BMI")

loop = 0
while loop < 3:

    h=float(input("Your height (cm) is "))
    w=float(input("Your weight (kg) is "))        

    BMI = w/((h/100)**2)
    print("Your BMI = ", BMI)

    if BMI < 16:
        print("Severely underweight")
    elif BMI <= 18.5:
        print("Underweight")
    elif BMI <= 25:
        print("Normal")
    elif BMI <= 30:
        print("Overweight")
    else:
        print("Obese")

    loop += 1
