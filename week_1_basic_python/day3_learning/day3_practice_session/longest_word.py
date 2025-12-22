sentence = 'hello my name is vivek kakadia and i am from surat. currently i am learning python.'

words = sentence.split()

longest_word = ''

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)