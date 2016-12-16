import csv
import numpy as math

csvfile = open('working_l2.csv')
reader = csv.DictReader(csvfile)
outfile = open('labeled_tsne.csv', "w+")
fieldnames = ['character', 'x', 'y', 'meaning', 'pinying']
writer = csv.DictWriter(outfile, fieldnames)
writer.writeheader()

lines = list(open("cedict_ts.u8"))
# max_x = 0
# max_y = 0
# for row in reader:
#     if math.abs(float(row['x'])) > max_x:
#         max_x = math.abs(float(row['x']))
#     if math.abs(float(row['y'])) > max_y:
#         max_y = math.abs(float(row['y']))
# print max_x, max_y
#
# csvfile.seek(0)
# reader.__init__(csvfile, delimiter=",")

for row in reader:
    character = row['character']
    print character
    meaning = ""
    pinying = ""
    for line in lines:
        traditional, blank, rest = line.partition(" ")
        simplified, blank, rest = rest.partition(" ")
        if simplified == character:
            pinying, blank, rest = rest.partition(" ")
            pinying = pinying.strip('[]')
            thing, blank, rest = rest.partition("/")
            meaning, blank, rest = rest.partition("/")
        # if traditional == character:
        #     print traditional
    writer.writerow({'character': character, 'x': row['x'], 'y': row['y'], 'meaning': meaning, 'pinying': pinying})
# writer.writerow(
#     {'character': character, 'x': str(float(row['x']) * 100 / max_x), 'y': str(float(row['y']) * 100 / max_y),
#      'meaning': meaning, 'pinying': pinying})
