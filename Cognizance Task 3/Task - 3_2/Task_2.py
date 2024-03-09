data = []
with open('data.csv', 'r') as f:
    for line in f:
        data.append(line.strip().split(','))


for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] in ['NaN', 'NA', '-', 'Nil']:
            data[i][j] = 0

with open('data_cleaned.csv', 'w') as f:
    for row in data:
        f.write(','.join(str(x) for x in row) + '\n')
