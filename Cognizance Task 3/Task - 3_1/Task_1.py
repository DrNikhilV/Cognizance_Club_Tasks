import re

with open('onelinefile.txt', 'r') as infile:
  data = infile.read()

pattern = r'(\d+)([A-Za-z]+)(\d\.\d+)([A-Za-z]+)'
tuples = re.findall(pattern, data)

with open('Filename2.csv', 'w') as outfile:
  for t in tuples:
    outfile.write(','.join(t) + '\n')
