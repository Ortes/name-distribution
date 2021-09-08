import csv
import math
import json

filename = 'nat2019.csv'


def get_letter_position(letter):
    return ord(letter) - ord('A')

tmpdata = [0] * 26
with open(filename, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in spamreader:
        if 1920 - 5 <= int(row[2]) <= 2005 + 5:
            tmpdata[get_letter_position(row[1][0])] += int(row[3])



for i in range(1995, 1996):
    ``

finalData = []
for sex in ["1", "2"]:
    sexdata = []

        data = [0] * 26

        with open(filename, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in spamreader:
                try:
                    if row[0] == sex and i - 5 <= int(row[2]) <= i + 5:
                        number = int(row[3])
                        data[get_letter_position(row[1][0])] += number
                except:
                    pass

        total = sum(data)

        # print(",".join([str(d[1]) for d in data.items()]))

        for l in data:
            if l == 0:
                l = math.log(1 / (1 / total), 2)
            else:
                data[l] = math.log(1 / (data[l] / total), 2)

        d = sorted(data)
        a = 400 / (d[25] - d[0])
        b = 500 - a * d[25]

        tmp = []
        for l in data:
            data[l] = a * data[l] + b
            tmp.append(int(round(data[l])))
            # print(l, data[l])

        sexdata.append(tmp)

        # print('Total names : \n', sum)
    finalData.append(sexdata)

f = open("year-data.json", "w")
f.write(json.dumps(finalData))
f.close()

print(json.dumps(finalData))

# for n in name.items():
#    print(n)
