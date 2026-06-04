# Variables of different data types
name = "Ariana"  # string 
age = 32         # integer
height = 1.53    # float
weight = 54      # integer
is_female = True # boolean

bmi = weight / (height**2)

if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi < 25:
    status = "Normal weight"
elif 25 <= bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

if is_female == True:
    gender = "Female"
else: 
    gender = "Male"

print(f"Report: {name.upper()}\n")
print(f"Age:    {age} years old")
print(f"Gender: {gender}")
print(f"Height: {height} m")
print(f"Weight: {weight} kg\n")
print(f"BMI:    {bmi:.0f}")
print(f"Status: {status}")
