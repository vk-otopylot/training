weight = int(input('Enter your weight in kg: '))
height = int(input('Enter your height in cm: '))

meters = height / 100
result = weight / (meters**2)

print('your BMI is', result)