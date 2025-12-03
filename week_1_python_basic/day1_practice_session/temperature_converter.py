user_inp = input('press 1 to convert temperature from Celsius to Fahrenheit \npress 2 to convert temperature from Fahrenheit to Celsius \n')

if user_inp == '1':
    temperature = float(input('Enter temperature in celsius: '))
    c_to_f = temperature * (9/5) + 32
    print(f'{temperature} celsius is equal to {c_to_f:.2f} Fahrenheit')

elif user_inp == '2':
    temperature = float(input('Enter temperature in Fahrenheit: '))
    f_to_c = (temperature-32) * 5/9
    print(f'{temperature} Fahrenheit is equal to {f_to_c:.2f} celsius')

else:
    print('Invalid choice')