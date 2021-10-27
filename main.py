import csv
import math
import json
import numpy as np

filename = 'nat2019.csv'
startYear = 1940
endYear = 2010
yearRange = endYear - startYear


def get_letter_position(letter):
    return ord(letter) - ord('A')


rawData = np.zeros((yearRange, 26, 2))
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        try:
            year = int(row[2])
            if startYear <= year <= endYear:
                sex = int(row[0]) - 1
                number = int(row[3])
                yearIndex = year - startYear
                letter = get_letter_position(row[1][0])

                rawData[yearIndex][letter][sex] += number
        except:
            pass


def reorder(total):
    def f(x):
        if x == 0:
            return math.log(total, 2)
        else:
            return math.log(1 / (x / total), 2)

    return f


finalData = np.zeros((yearRange - 10, 26, 2))
for i in range(4, yearRange - 5):
    centeredMatrix = rawData[np.ix_(range(i - 5, i + 5))]
    summedMatrix = centeredMatrix.sum(axis=0)
    total = summedMatrix.sum()
    transformedMatrix = np.vectorize(reorder(total))(summedMatrix)
    transformedMatrix.sort(axis=0)
    a = 400 / (transformedMatrix[25] - transformedMatrix[0])
    b = 500 - a * transformedMatrix[25]
    finalData[i - 5] = transformedMatrix * a + b


finalData = finalData.tolist()
f = open("year-data.json", "w")
f.write(json.dumps(finalData))
f.close()

print(json.dumps(finalData))
