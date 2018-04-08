import csv
import numpy as np
import matplotlib.pyplot as plt
import random

toread = ["Fake_Binary_Data.csv"]
alldata = {}

current_person = None
for r in toread:
  with open(r, 'rt') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    binaryqs = {}
    for row in spamreader:
      if row[0] == 'Name':
        if current_person:
          alldata[current_person.strip()] = binaryqs
          current_person = row[1]
          binaryqs = {}
        else:
          current_person = row[1]
      elif row[0] != "Question":
        binaryqs[row[0]] = "yes" if random.random() < 0.5 else "no" # random inputs for now
        # binaryqs[row[0]] = row[1] # the actual code
  alldata[current_person] = binaryqs
  current_person = None

data = list(alldata.values())
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


if graph == "histogram" and len(inps) > 1:
  N = len(inps)
  yes = []
  no = []
  for i in range(len(inps)):
    yes.append(len([d for d in data if d[inps[i]] == 'yes']) / len(data))
    no.append(1 - yes[i])

  ind = np.arange(N)
  width = 0.35

  p1 = plt.bar(ind, yes, width)
  p2 = plt.bar(ind, no, width, bottom = yes)

  plt.ylabel('Number of People')
  plt.title(", ".join(inps))
  plt.xticks(ind, inps)
  plt.yticks(np.arange(0, 1.1, 0.1))
  plt.legend((p1[0], p2[0]), ('yes', 'no'))

  plt.show()




'''

some sample code im working with to make multi person dicts

'''
