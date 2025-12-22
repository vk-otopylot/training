# Remove Duplicates

# nums = [1, 2, 2, 3, 4, 4, 5]
#
# result = set(nums)
#
# print(result)


# Common Elements

# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}
#
# set3 = set1 & set2
# print(set3)


# Unique Elements from both sets

# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}
#
# set1.union(set2)
#
# print(set1)


# Elements Only in First Set.

# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7}
#
# C = A-B
#
# print(C)


# Check Subset

main_set = {1, 2, 3, 4, 5, 6}
child_set = {2, 4, 6}

print(f'child_set is subset of main_set: {child_set.issubset(main_set)}')