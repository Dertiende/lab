import random
import numpy as np


def orient_generate_edges(nodes): #weak
    matrix = np.zeros((nodes, nodes))
    for i in range(nodes):
        for j in range(nodes):
            ves = random.randint(0, 1)
            if i != j:
                matrix[i][j] = ves
    try:
        file = open("gen.csv", "w")
        for i in range(nodes):
            file.write(str(i) + ";")
            for j in range(nodes):
                try:
                    if matrix[i][j] != 0:
                        file.write(str(j) + ";")
                except Exception as e:
                    print("can't write to file: ", e)
                    file.close()
            file.write("\n")
        file.close()
    except Exception as e:
        print("can't open file: ", e)
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
        try:
            file = open("gen.csv", "w")
            for i in range(nodes):
                file.write(str(i) + ";")
                for j in range(nodes):
                    try:
                        if matrix[i][j] != 0:
                            file.write(str(j)+" *"+str(matrix[i][j]) +"*"+ ";")
                    except Exception as e:
                        print("can't write to file: ", e)
                        file.close()
                file.write("\n")
            file.close()
        except Exception as e:
            print("can't open file: ", e)
        return matrix


def norient_generate_edges_ves(nodes): #strong
        matrix = np.zeros((nodes, nodes))
        for i in range(nodes):
            for j in range(i + 1, nodes):

                ves = random.randint(0, 1)
                if i != j and ves == 1:
                    matrix[i][j] = random.randint(0, 1000)
        for i in range(nodes-1,0, -1):
            for j in range(nodes-1):
                matrix[i][j] = matrix[j][i]
        try:
            file = open("gen.csv", "w")
            for i in range(nodes):
                file.write(str(i) + ";")
                for j in range(nodes):
                    try:
                        if matrix[i][j] != 0:
                            file.write(str(j)+" *"+str(matrix[i][j]) +"*"+ ";")
                    except Exception as e:
                        print("can't write to file: ", e)
                        file.close()
                file.write("\n")
            file.close()
        except Exception as e:
            print("can't open file: ", e)

        return matrix



print(norient_generate_edges_ves (10))
