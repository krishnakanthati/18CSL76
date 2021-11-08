# candidate elimination algorithm

import csv

# Read the enjoysport csv file
file = open('enjoysport.csv')
data = list(csv.reader(file))[1:]

concepts = []
target = []

# concepts is the list of instances
# target is the list of target values
for i in data:
    concepts.append(i[:-1])
    target.append(i[-1])

# Define the most specific and most general hypothesis
specific_h = ['0'] * len(concepts[0])
a = range(len(specific_h))
general_h = [['?' for i in a] for i in a]

for i, instance in enumerate(concepts):
    if target[i] == 'yes':
        for x in a:
            if specific_h[x] == '0':
                specific_h[x] = instance[x]
            elif instance[x] != specific_h[x]:
                specific_h[x] = '?'
                general_h[x][x] = '?'
    elif target[i] == 'no':
        for x in a:
            general_h[x][x] = specific_h[x] if instance[x] != specific_h[x] else '?'

indices = [i for i, val in enumerate(general_h) if val == ['?'] * len(concepts[0])]

for i in indices:
    general_h.remove(['?'] * len(concepts[0]))

print('Final Specific: ', specific_h)
print('Final General: ', general_h)
