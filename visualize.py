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

graphs = ["histogram", "line", "scatter", "tables"]
graph = ""
inps = []

while True:
  while True:
    graph = input("enter type of graph: ").lower()
    if graph in graphs:
      break
    else:
      print("please enter one of the following: %s" % (", ".join(graphs)))

  inps = input("enter data types separated by commas: ").split(",")
  inps = [i.strip() for i in inps]
  yn = input("%s with data type(s) '%s'? y/n: " % (graph, ", ".join(inps))).lower()
  if yn == "yes" or yn == "y":
    break

if graph == "histogram" and len(inps) == 1:
  yes = len([d for d in data if d[inps[0]] == 'yes'])

  x = np.arange(2)
  y = [yes, len(data) - yes]

  fig, ax = plt.subplots()
  plt.bar(x, y)
  plt.xticks(x, ('yes', 'no'))
  plt.ylabel('number of people')
  plt.title(inps[0])
  plt.show()

# elisa!! inps is list of data types - pls make fancy bar graph :)
if graph == "histogram" and len(inps) > 1:
  pass



