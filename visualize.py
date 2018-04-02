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
      binaryqs[row[0]] = "yes" if random.random() < 0.5 else "no" # random inputs for now
      # binaryqs[row[1]] = row[0] # the actual code
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
