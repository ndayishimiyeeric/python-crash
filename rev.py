text = input()

textList = text.split(" ")
longest_word = ''
count = 0

for word in textList:
    if (len(word) > 0):
        count = len(word)
        longest_word = word

print(longest_word)
