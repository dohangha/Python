import pandas as pd
import re
import statistics

# cau1
filename = input("Enter a class to grade (i.e. class1 for class1.txt): ")
filename1 = filename
filename = filename + '.txt'

try:
    with open(filename, "r") as file:
        data = file.read()
        print('Successfully opened: ', filename)
except IOError:
    print("File cannot be found.")

# cau2
data_regex = []
lines = data.split()
totalinvalid = 0
for line in lines:
    words = line.split(',')
    if len(words) != 26:
        print('Invalid line of data: does not contain exactly 26 values:')
        print(line)
        totalinvalid += 1
    else:
        pattern = 'N[0-9]{8,}'
        data1 = [x for x in words if re.match(pattern, x) != None]
        if len(data1) == 0:
            print('Invalid line of data: N# is invalid')
            print(line)
            totalinvalid += 1
        else:
            data_regex.append(line)
print('Total valid lines of data:', len(lines) - totalinvalid)
print('Total invalid lines of data:', totalinvalid)
# Cau3, cau 4
answer_key = {1: 'B', 2: 'A', 3: 'D', 4: 'D', 5: 'C', 6: 'B', 7: 'D', 8: 'A', 9: 'C', 10: 'C', 11: 'D', 12: 'B',
              13: 'A', 14: 'B', 15: 'A', 16: 'C', 17: 'B', 18: 'D', 19: 'A', 20: 'C', 21: 'A', 22: 'A', 23: 'B',
              24: 'D', 25: 'D'}
correct = 0
diem = 0
splitscore = []
list_score = []
f = open(filename1 + "_grades.txt", "w+")

for line in data_regex:
    diem = 0
    for i, result in enumerate(line.split(',')[1:]):
        correct += 1
        if result == answer_key[i + 1]:
            diem += 4
        elif result != '':
            diem += -1
    splitscore.append(diem)
    f.writelines(line.split(',')[0] + "," + str(diem) + '\n')
f.close()
print('Mean (average) score: ', diem)
print('Highest score: ', max(splitscore))
print('Lowest score: ', min(splitscore))
print('Range of scores: ', max(splitscore) - min(splitscore))
print('Median score: ', statistics.median(splitscore))






