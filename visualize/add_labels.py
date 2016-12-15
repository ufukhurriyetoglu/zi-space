import csv
import codecs

csvfile = open('tsne.csv')
reader = csv.DictReader(csvfile)
outfile = open('labeled_tsne.csv', "w+")
fieldnames = ['character', 'x', 'y', 'meaning', 'pinying']
writer = csv.DictWriter(outfile, fieldnames)
writer.writeheader()

lines = list(open("cedict_ts.u8"))

for row in reader:
    character = row['character']
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
