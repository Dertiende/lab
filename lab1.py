import random
import numpy as np
from SCC import kosaraju

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
    uncon =[i for i in range(nodes)]
    con = []
    matrix = np.zeros((nodes, nodes))
    for i in range(nodes):
        for j in range(i + 1, nodes):

            ves = random.randint(0, 1)
            if i != j:
                matrix[i][j] = ves
    for i in range(nodes):
        for j in range (i+1, nodes):
            if i != j and matrix[i][j] != 0:
                if len(con)==0:
                    con.append(i)
                    con.append(j)
                a = con.count(i)
                b = con.count(j)
                if a == 0 or b == 0:
                   if a == 0 and b != 0: con.append(i)
                   if b == 0 and a != 0: con.append(j)
    con.sort()
    print ("unc",uncon)
    print (con)


    for i in range(nodes - 1, 0, -1):
        for j in range(nodes - 1):
            matrix[i][j] = matrix[j][i]



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




if __name__ == '__main__':
    print ("Введите кол-во вершин: ")
    nodes = int(input())
    print("Граф ориентированный?\n 1 - да\n 0 - нет")
    orient = int(input())
    print ("Генерировать вес ребра?\n 1 - да\n 0 - нет")
    ves = int(input())
    if orient == 1:
        if ves == 1:
            print(orient_generate_edges_ves(nodes))
        else: print(orient_generate_edges(nodes))
    else:
        if ves == 1:
            print(norient_generate_edges_ves(nodes))
        else: print(norient_generate_edges(nodes))