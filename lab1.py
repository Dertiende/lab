import random
import numpy as np


def orient_generate_edges(nodes): #weak
    matrix = np.zeros((nodes, nodes))
    for i in range(nodes):
        for j in range(nodes):
            ves = random.randint(0, 1)
            if i != j:
                matrix[i][j] = ves
    return matrix


def norient_generate_edges(nodes): #strong
    matrix = np.zeros((nodes, nodes))
    for i in range(nodes):
        for j in range(i + 1, nodes):

            ves = random.randint(0, 1)
            if i != j:
                matrix[i][j] = ves
    return matrix

def orient_generate_edges_ves (nodes): #weak
        matrix = np.zeros((nodes, nodes))
        for i in range(nodes):
            for j in range(nodes):
                ves = random.randint(0, 1)
                if i != j and ves == 1:
                    matrix[i][j] = random.randint(0, 1000)
        return matrix


def norient_generate_edges_ves(nodes): #strong
        matrix = np.zeros((nodes, nodes))
        for i in range(nodes):
            for j in range(i + 1, nodes):

                ves = random.randint(0, 1)
                if i != j and ves == 1:
                    matrix[i][j] = random.randint(0, 1000)
        return matrix

#def ns_con_generate_edges(): #not stated
#def generate_edges(graph):

    #edges = []
    # for each node in graph
    #for node in graph:

        # for each neighbour node of a single node
        #for neighbour in graph[node]:
            # if edge exists then append
            #edges.append((node, neighbour))
    #return edges
print(orient_generate_edges (10))
