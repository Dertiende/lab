import random
import numpy as np


def orient_generate_edgessss(nodes):
    matrix = np.zeros((nodes, nodes))
    for i in range(nodes):
        for j in range(nodes):
            ves = random.randint(0,1)
            if i != j and ves==1:
                matrix[i][j]= random.randint(0,1000)
    return matrix

def orient_generate_edges(nodes):
    matrix = np.zeros((nodes, nodes))
    for i in range(nodes):
        for j in range(i+1, nodes):

            ves = random.randint(0,1)
            if i != j and ves==1:
                matrix[i][j]= random.randint(0,1000)
    return matrix

print(orient_generate_edges(10))
