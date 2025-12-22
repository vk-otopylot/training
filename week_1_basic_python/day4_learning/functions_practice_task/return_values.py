# Maximum of Two Numbers

# def max_of_two(a,b):
#     if a > b:
#         return a
#     else:
#         return b
#
# print('max is',max_of_two(5,52))

# Area of Rectangle

# def area(length, width):
#     return length * width
#
# print(area(5,9))

# Sum of List Elements

def sum_list(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

nums = [1,9,8,54,86,6]
print(sum_list(nums))