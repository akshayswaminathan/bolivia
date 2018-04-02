import csv
import numpy as np
import matplotlib.pyplot as plt
import random

toread = ["Fake_Binary_Data.csv"] * 50 # reading the same file 50 times over
data = []

for r in toread:
  binaryqs = {}
  with open(r, 'rt') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
      #binaryqs[row[1]] = "yes" if random.random() < 0.5 else "no" # random inputs for now
      binaryqs[row[1]] = row[0] # the actual code
      person = row[0]
  data.append(binaryqs)

# example bar graph for chicken pox
yes = len([d for d in data if d['have chicken pox'] == 'yes'])

x = np.arange(2)
y = [yes, len(data) - yes]

fig, ax = plt.subplots()
plt.bar(x, y)
plt.xticks(x, ('have had chicken pox', 'haven\'t had chicken pox'))
plt.ylabel('number of people')
plt.show()

'''
with open("data.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in readCSV:
        person = row[0]
        # Initializes only one person dict
        if person not in final:
            final[person] = {f: 0 for f in fruitToAnalyze}
        fruit_counter = final[person]
        fruit = row[1].strip()
        if fruit in fruitToAnalyze:
            fruit_counter[fruit] += 1 '''
