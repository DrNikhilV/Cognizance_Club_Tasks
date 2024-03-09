with open('about.txt', 'r') as f:
  contents = f.read()
  
words = contents.split()


word_count = {}

for word in words:
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1


most_common_word = None
highest_frequency = 0
for word, frequency in word_count.items():
  if frequency > highest_frequency:
    most_common_word = word
    highest_frequency = frequency

print(f'The most frequently used word is "{most_common_word}" .')

count = 0
for word in words:
  if len(word) >= 6:
    count += 1
print(f'There are {count} words with at least 6 letters.')
