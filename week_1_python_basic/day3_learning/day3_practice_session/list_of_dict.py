key = ['name', 'age', 'gender']
value = [('vivek', 20, 'male'), ('dharmesh', 28, 'male'), ('mayur', 30, 'male')]

print(value[0][0])

for v in range(len(value)):
    for k in range(len(key)):
        for l in range(len(value[v])):
            print(f'{key[l]}:{value[v][l]}')
