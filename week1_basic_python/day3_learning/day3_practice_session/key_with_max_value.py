numbers = {
    'ten': 10,
    'seventy': 70,
    'sixty': 60,
    'thirty': 30,
    'fifty': 50,
}

# largest_key = 0
#
# for value in numbers.keys():
#     if value > largest_key:
#         largest_key = value
#
# print(largest_key)

max_value = max(numbers.values())

for key,value in numbers.items():
    if value == max_value:
        print(f'{key}: {value}')