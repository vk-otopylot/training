unit = int(input('Enter your total usage unit to know price per unit: '))

if unit >= 0 and unit <= 100:
    print('₹5/unit')

elif unit >= 101 and unit <= 200:
    print('₹7/unit')

elif unit >= 201 and unit <= 300:
    print('₹10/unit')

else:
    print('₹15/unit')