key = ['name', 'age', 'gender']
value = [('vivek', 20, 'male'), ('dharmesh', 28, 'male'), ('mayur', 30, 'male')]

# print(value[0][0])
# print(key[0])

# for v in range(len(value)):
#         # print(k)
#         for j in value:
#             for m in j:
#                 print(f'{key[v]}:{m}')
        # for k in value:
        #     # print(k)
        #     for j in k:
        #         # print(j)
        #         for m in key:
        #             print(f'{m}:{j}')

    # for k in range(len(key)):
    #     for l in range(len(value[v])):
    #         print(f'{key[l]}:{value[v][l]}')


result = [ dict(zip(key, v)) for v in value ]

print(result)