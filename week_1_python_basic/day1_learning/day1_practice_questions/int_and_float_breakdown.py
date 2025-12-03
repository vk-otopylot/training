no = float(input('Enter any float number: '))

integer_part = int(no)

decimal_part = no - integer_part

print("Original number:", no)
print("Integer part:", integer_part)
print("Decimal part:%.2f" % (decimal_part))

