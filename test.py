import random


ves = []

for i in range ( 10):
    a = random.randint(1, 1000)
    ves.append([])
    for j in range (5):
        ves[i].append({j:random.randint(1,100)})
print (ves)