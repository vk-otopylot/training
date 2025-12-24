# Extract unique vowels from a word

# text = "programming"
# n_set = {x for x in text if x in('a','e','i','o','u')}
# print(n_set)


# Remove duplicates & convert to uppercase

# li = ["apple","Apple","banana","BANANA"]
# n_set = {x.upper() for x in li}
# print(n_set)


# Intersection — values present in both lists

# li1 = [1,2,3,4]
# li2 = [3,4,5,6]
# n_set = {x for x in li1 if x in li2}
# print(n_set)


# Create set of word lengths

# li = ["cat","tiger","lion"]
# n_set = {len(x) for x in li}
# print(n_set)


# Filter unique numbers greater than 50

li = [10,55,32,80,55,90]
n_set = {x for x in li if x>50}
print(n_set)