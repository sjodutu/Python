'''
Height = float(input("Enter yor height in centimeters: "))
Weight = float(input("Enter your weight in kg: "))
Height = Height/100
BMI = Weight/(Height * Height)
print(f"your body mass index is:  {BMI}")
if BMI > 0:
        if BMI <= 16:
            print('You are serverly underweight')
        elif BMI <= 18.5:
            print("you are underweight")
        elif BMI <= 25:
            print("you are Healthy")
        elif BMI <= 30:
            print("you are overweight")
        else: print("you are severely overweight")
else:("Enter valid details")
'''
Height = float(input("Enter your height in meters: "))
Weight = float(input("Enter you weight in kilograms: "))
BMI = Weight/(Height*Height)
print(f"Your height is {Height}, your weight is {Weight} and your BMI is {BMI}")