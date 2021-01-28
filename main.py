import csv

data = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0,
    'J': 0,
    'K': 0,
    'L': 0,
    'M': 0,
    'N': 0,
    'O': 0,
    'P': 0,
    'Q': 0,
    'R': 0,
    'S': 0,
    'T': 0,
    'U': 0,
    'V': 0,
    'W': 0,
    'X': 0,
    'Y': 0,
    'Z': 0,
}

name = dict()

filename = 'data.csv'
with open(filename, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in spamreader:
        try:
            if row[0] == '2' and 1990 <= int(row[2]) <= 2000:
                number = int(row[3])
                if row[1] in name:
                    name[row[1]] += number
                else:
                    name[row[1]] = number
                data[row[1][0]] += number
        except:
            pass

sum = 0
for l in data.items():
    sum += l[1]

for l in data.items():
    print(l[0], (l[1] / sum) * 100.0)

print('Total names : ', sum)


for n in name.items():
    print(n)
