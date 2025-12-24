# Square of a Number Using Lambda

# square = lambda x : x * x
#
# print(square(4))


# Find Maximum of Two Numbers Using Lambda

# max_of_two = lambda x, y : x if x > y else y
#
# print(max_of_two(12,5))


# Convert List of Strings to Uppercase

# li = ['vivek', 'shani', 'hardeep', 'ayush']
#
# result = list(map(lambda x : x.upper(), li))
#
# print(result)


# Sum of Squares of Even Numbers

li = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda x: x%2 == 0, li))

square = list(map(lambda x : x * x, even))

print(sum(square))