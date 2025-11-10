import string

words = []
while True:
    word = input("Enter a word: ")
    if word == '':
        break
    for ch in string.punctuation:
        word = word.replace(ch, '')
    words.extend(word.lower().split())
count = {}
order = []
for w in words:
    if w not in count:
        count[w] = 0
        order.append(w)
    count[w] += 1
sorted_words = sorted(order, key=lambda x: (-count[x], order.index(x)))
for w in sorted_words:
    print(w)
