import string

sentences = input()
for punctuation_marks in string.punctuation:
    sentences = sentences.replace(punctuation_marks, '')
print(list(set(sentences.split())))