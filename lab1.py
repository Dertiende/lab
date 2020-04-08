import random

import numpy as np
from SCC import kosaraju
from importer import csv_to_dict


def orient_generate_edges(connect, nodes, strong,start=1):  # weak
    matrix = []
    for i in range(nodes):
        matrix.append([])
        for j in range(nodes):
            matrix[i].append(0)
    print("Генерируем граф", end="")
    for i in range(nodes):
        if i % 20 == 0:
            print(".", end="")
        for j in range(nodes):
            ves = random.randint(0, 1)
            if i != j:
                matrix[i][j] = ves
    print("[ОК]")
    if connect:
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


def norient_generate_edges(connect, nodes):  # strong
    chance = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    matrix = []
    for i in range(nodes):
        matrix.append([])
        for j in range(nodes):
            matrix[i].append(0)
    print("Генерируем граф", end="")
    for i in range(nodes):
        if i % 20 == 0:
            print(".", end="")
        for j in range(i + 1, nodes):
            ves = random.choice(chance)
            if i != j:
                matrix[i][j] = ves

    for i in range(nodes - 1, 0, -1):
        for j in range(nodes - 1):
            matrix[i][j] = matrix[j][i]
    print("[ОК]")
    if connect:
        matrix = solo_edge(matrix, nodes, 0)

    try:
        file = open("gen.csv", "w")
        for i in range(nodes):
            file.write("["+str(i) +"]"+ ";")
            for j in range(nodes):
                try:
                    if matrix[i][j] != 0:
                        file.write("["+ str(j) +"]"+ ";")
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


def orient_generate_edges_ves(connect, nodes, strong, start=1):
    matrix = []
    for i in range(nodes):
        matrix.append([])
        for j in range(nodes):
            matrix[i].append(0)
    if start: print("Генерируем граф", end="")
    for i in range(nodes):
        if i % 20 == 0:
            print(".", end="")
        for j in range(nodes):
            ves = random.randint(0, 1)
            if i != j and ves == 1:
                matrix[i][j] = random.randint(0, 1000)
    if start: print("[ОК]")
    if connect:
        matrix = solo_edge(matrix, nodes, 1, 1)

    try:
        file = open("gen.csv", "w")
        for i in range(nodes):
            file.write("[" + str(i) + "]" + ";")
            for j in range(nodes):
                try:
                    if int(matrix[i][j]) != int(0):
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
            orient_generate_edges_ves(connect,nodes, 1)
        if len(kosaraju(kosadict)) == 1:print("[ОК]")
        return matrix


    else:

        return matrix


def norient_generate_edges_ves(connect, nodes):  # strong
    chance = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    matrix = []
    for i in range(nodes):
        matrix.append([])
        for j in range(nodes):
            matrix[i].append(0)
    print("Генерируем граф", end="")
    for i in range(nodes):
        if i % 20 == 0:
            print(".", end="")
        for j in range(i + 1, nodes):
            ves = random.choice(chance)
            if i != j and ves == 1:
                matrix[i][j] = random.randint(0, 1000)
    for i in range(nodes - 1, 0, -1):
        for j in range(nodes - 1):
            matrix[i][j] = matrix[j][i]
    print("[ОК]")
    if connect:
        matrix = solo_edge(matrix, nodes, 1)

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
    print("Граф связный?\n 1 - да\n 0 - нет")
    connect = int(input())
    print("Генерировать вес ребра?\n 1 - да\n 0 - нет")
    ves = int(input())
    if orient == 1:
        print("Граф сильносвязный?\n 1 - да\n 0 - нет")
        strong = int(input())
        if ves == 1:
            out = orient_generate_edges_ves(connect, nodes, strong)
            for i in range(nodes):
                print(out[i])
        else:
            out = orient_generate_edges(connect, nodes, strong)
            for i in range(nodes):
                print(out[i])
    else:
        if ves == 1:
            out = norient_generate_edges_ves(connect, nodes)
            for i in range(nodes):
                print(out[i])
        else:
            out = norient_generate_edges(connect, nodes)
            for i in range(nodes):
                print(out[i])
    return nodes,out


if __name__ == '__main__':
    # orient_generate_edges(1000,0)
    generate()
