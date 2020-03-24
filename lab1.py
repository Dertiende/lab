import random

import numpy as np
from SCC import kosaraju
from importer import csv_to_dict


def orient_generate_edges(nodes, strong,start=1):  # weak
    matrix = np.zeros((nodes, nodes))
    print("Генерируем граф", end="")
    for i in range(nodes):
        if i % 20 == 0:
            print(".", end="")
        for j in range(nodes):
            ves = random.randint(0, 1)
            if i != j:
                matrix[i][j] = ves
    print("[ОК]")

    matrix = solo_edge(matrix, nodes, 0, 1)

    try:
        file = open("gen.csv", "w")
        for i in range(nodes):
            file.write("[" + str(i) + "]" + ";")
            for j in range(nodes):
                try:
                    if matrix[i][j] != 0:
                        file.write("[" + str(j) + "]" + ";")
                except Exception as e:
                    print("can't write to file: ", e)
                    file.close()
            file.write("\n")
        file.close()
    except Exception as e:
        print("can't open file: ", e)
    print("CSV-файл создан")
    if strong and start:print("Проверяем сильносвязность", end="")
    if strong:
        kosadict = csv_to_dict(nodes)
        while len(kosaraju(kosadict)) != 1:
            print(".", end="")
            orient_generate_edges_ves(nodes, 1)
            # print("hell")
        if len(kosaraju(kosadict)) == 1:print("[ОК]")
        return matrix

    else:

        return matrix


def solo_edge(matrix, nodes, ves, orient):
    maybe = []
    solo = []
    print("Проверяем связность", end="")
    for j in range(nodes):
        if j % 50 == 0:
            print(".", end="")
        if int(matrix[0][j]) == 0:
            i = 0
            while int(matrix[i][j]) == 0:
                i = i + 1
                if i == nodes:
                    maybe.append(j)
                    break

    for i in maybe:
        if i % 50 == 0:
            print(".", end="")
        if int(matrix[i][0]) == 0:
            j = 0
            while int(matrix[i][j]) == 0:
                j = j + 1
                if j == nodes:
                    solo.append(i)
                    break
    for i in solo:
        if i % 20 == 0:
            print(".", end="")
        if orient:
            a = random.randint(0, 1)
            if a:
                if not ves:
                    matrix[i][random.randint(0, nodes - 1)] = 1
                else:
                    matrix[i][random.randint(0, nodes - 1)] = random.randint(0, 1000)
            else:
                if not ves:
                    matrix[random.randint(0, nodes - 1)][i] = 1
                else:
                    matrix[random.randint(0, nodes - 1)][i] = random.randint(0, 1000)
        else:
            a = random.randint(0, 1000)
            if a:
                if not ves:
                    matrix[i][random.randint(0, nodes - 1)] = 1
                    matrix[random.randint(0, nodes - 1)][i] = 1
                else:
                    matrix[i][random.randint(0, nodes - 1)] = random.randint(0, a)
                    matrix[random.randint(0, nodes - 1)][i] = random.randint(0, a)
    print("[ОК]")
    return matrix


def norient_generate_edges(nodes):  # strong
    matrix = np.zeros((nodes, nodes))
    print("Генерируем граф", end="")
    for i in range(nodes):
        if i % 20 == 0:
            print(".", end="")
        for j in range(i + 1, nodes):
            ves = random.randint(0, 1)
            if i != j:
                matrix[i][j] = ves

    for i in range(nodes - 1, 0, -1):
        for j in range(nodes - 1):
            matrix[i][j] = matrix[j][i]
    print("[ОК]")

    matrix = solo_edge(matrix, nodes, 0)

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
    print("CSV-файл создан")

    # print(matrix)

    return matrix


def orient_generate_edges_ves(nodes, strong, start=1):
    matrix = np.zeros((nodes, nodes))
    if start: print("Генерируем граф", end="")
    for i in range(nodes):
        if i % 20 == 0:
            print(".", end="")
        for j in range(nodes):
            ves = random.randint(0, 1)
            if i != j and ves == 1:
                matrix[i][j] = random.randint(0, 1000)
    if start: print("[ОК]")
    solo_edge(matrix, nodes, 1, 1)

    try:
        file = open("gen.csv", "w")
        for i in range(nodes):
            file.write("[" + str(i) + "]" + ";")
            for j in range(nodes):
                try:
                    if matrix[i][j] != 0:
                        file.write("[" + str(j) + "]" + " *" + str(matrix[i][j]) + "*" + ";")
                except Exception as e:
                    print("can't write to file: ", e)
                    file.close()
            file.write("\n")
        file.close()
    except Exception as e:
        print("can't open file: ", e)
    print("CSV-файл создан")
    if strong and start:print("Проверяем сильносвязность", end="")
    if strong:

        kosadict = csv_to_dict(nodes)
        while len(kosaraju(kosadict)) != 1:
            print(".", end="")
            orient_generate_edges_ves(nodes, 1)
        if len(kosaraju(kosadict)) == 1:print("[ОК]")
        return matrix


    else:

        return matrix


def norient_generate_edges_ves(nodes):  # strong
    matrix = np.zeros((nodes, nodes))
    print("Генерируем граф", end="")
    for i in range(nodes):
        if i % 20 == 0:
            print(".", end="")
        for j in range(i + 1, nodes):
            ves = random.randint(0, 1)
            if i != j and ves == 1:
                matrix[i][j] = random.randint(0, 1000)
    for i in range(nodes - 1, 0, -1):
        for j in range(nodes - 1):
            matrix[i][j] = matrix[j][i]
    print("[ОК]")
    solo_edge(matrix, nodes, 1)

    try:
        file = open("gen.csv", "w")
        for i in range(nodes):
            file.write("[" + str(i) + "]" + ";")
            for j in range(nodes):
                try:
                    if matrix[i][j] != 0:
                        file.write("[" + str(j) + "]" + " *" + str(matrix[i][j]) + "*" + ";")
                except Exception as e:
                    print("can't write to file: ", e)
                    file.close()
            file.write("\n")
        file.close()
    except Exception as e:
        print("can't open file: ", e)
    print("CSV-файл создан")

    return matrix


def generate():
    print("Введите кол-во вершин: ")
    nodes = int(input())
    print("Граф ориентированный?\n 1 - да\n 0 - нет")
    orient = int(input())
    print("Генерировать вес ребра?\n 1 - да\n 0 - нет")
    ves = int(input())
    if orient == 1:
        print("Граф сильносвязный?\n 1 - да\n 0 - нет")
        strong = int(input())
        if ves == 1:
            print(orient_generate_edges_ves(nodes, strong))
        else:
            print(orient_generate_edges(nodes, strong))
    else:
        if ves == 1:
            print(norient_generate_edges_ves(nodes))
        else:
            print(norient_generate_edges(nodes))
    return nodes


if __name__ == '__main__':
    # orient_generate_edges(1000,0)
    generate()
