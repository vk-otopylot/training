# Square all numbers in a list

# li = [1,2,3,4,5,6,7,8,9,10]
#
# n_list = [x * x for x in li]
#
# print(n_list)

# Extract only even numbers from a list

# li = [1,2,3,4,5,6,7,8,9,10]
#
# n_list = [ x for x in li if x%2==0]
# print(n_list)


# Convert list of words to length of each word

# li = ["python","map","code"]
#
# n_list = [len(x) for x in li]
# print(n_list)


# Create list of squares only for even numbers

# li = [1,2,3,4,5,6,7,8,9,10]
#
# n_list = [x*x for x in li if x%2==0]
# print(n_list)

# Extract first letter of each word

# li = ["Dog","Tiger","Lion"]
#
# n_list = [x[0] for x in li]
# print(n_list)


# Flatten a nested list (1 level deep)

# li = [[1,2],[3,4],[5,6]]
#
# n_list = [z for x in li for z in x]
# print(n_list)


# Generate list of tuples (number, square)

# li = [1,2,3,4]
#
# n_list = [(x,x*x) for x in li]
# print(n_list)

# Replace numbers < 0 with 0

li = [5,-3,8,-1,2]
n_list = [0 if item<0 else item for item in li]
print(n_list)