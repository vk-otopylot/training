# Square Using Lambda

# result = lambda x : x ** 2
#
# print(result(9))

# Add Two Numbers

# add = lambda x, y : x + y
#
# print(add(5,6))

# Even or Odd Using Lambda

# res = lambda x : 'even' if x % 2 == 0 else 'odd'
#
# print(res(5))

# Sort List of Tuples by the second value

# data = [(1, 3), (4, 1), (2, 2)]
#
# result = sorted(data, key=lambda x : x[1])
#
# print(result)

# Use lambda with filter to get only even number from list

def only_even(num):
    res = list(filter(lambda x : x % 2 == 0, num))
    return res

numbers = [1,2,3,4,5,6,7,8,9,10]
result = only_even(numbers)
print(result)