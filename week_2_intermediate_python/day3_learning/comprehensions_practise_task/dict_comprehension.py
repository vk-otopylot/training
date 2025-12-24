# Create dictionary of number → square

# li = [1,2,3,4,5]
#
# dict1 = {x:x*x for x in li}
# print(dict1)


# Convert list of words to dictionary word → length

# li = ["apple","banana","kiwi"]
#
# dict1 = {x: len(x) for x in li}
# print(dict1)

# Filter dictionary to keep only values > 50

# dict1 = { "a":20, "b":60, "c":45, "d":80 }
#
# n_dict = {k:v for k,v in dict1.items() if v>50}
# print(n_dict)

# Swap keys & values in dictionary

# dict1 = {1:"one",2:"two",3:"three"}
# n_dict = {v:k for k,v in dict1.items()}
# print(n_dict)

# Create dictionary of character → frequency

# text = "programming"
# dict1 = {k:text.count(k) for k in text}
# print(dict1)

# Convert temperature from Celsius → Fahrenheit

# dict1 = { "Delhi": 25, "Mumbai": 30 }
# dict2 = {k:(v * 9/5) + 32 for k,v in dict1.items()}
# print(dict2)

# Dictionary of number → even / odd label

li = [1,2,3,4,5]
n_dict = {k:'even' if k%2==0 else 'odd' for k in li}
print(n_dict)