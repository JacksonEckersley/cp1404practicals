

word_count = {}
word_in = input("Enter a string to count the occurrences of words in it: ")
words = word_in.split()

for word in words:
    frequency = word_count.get(word, 0)
    word_count[word] = frequency + 1

words = list(word_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_count[word]))
