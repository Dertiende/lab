import random

import numpy as np
from SCC import kosaraju
from importer import csv_to_dict

def orient_generate_edges(nodes,strong): #weak
    uncon = [i for i in range(nodes)]
    con = []
    matrix = np.zeros((nodes, nodes))
    print("Генерируем граф", end="")
    for i in range(nodes):
        if i%20==0:
            print(".", end="")
        for j in range(nodes):
            ves = random.randint(0, 1)
            if i != j:
                matrix[i][j] = ves
    print("[ОК]")
    print("Проверяем связность", end="")
    for i in range(nodes):
        if i%50==0:
            print(".", end="")
        for j in range (nodes):
            if i != j and matrix[i][j] != 0:
                if len(con)==0:
                    con.append(i)
                    con.append(j)
                    uncon.remove(i)
                    uncon.remove(j)
                a = con.count(i)
                b = con.count(j)
                if a == 0 or b == 0:
                   if a == 0 and b != 0:
                       con.append(i)
                       uncon.remove(i)
                   if b == 0 and a != 0:
                        con.append(j)
                        uncon.remove(j)
    for i in range(nodes-1,0,-1):
        if i%50==0:
            print(".", end="")
        for j in range (nodes):
            if i != j and matrix[i][j] != 0:
                if len(con)==0:
                    con.append(i)
                    con.append(j)
                    uncon.remove(i)
                    uncon.remove(j)
                a = con.count(i)
                b = con.count(j)
                if a == 0 or b == 0:
                   if a == 0 and b != 0:
                       con.append(i)
                       uncon.remove(i)
                   if b == 0 and a != 0:
                        con.append(j)
                        uncon.remove(j)
    con.sort()
    print("[ОК]")
    #print ("unc",uncon)
    #print (con)
    #print(matrix)


    for i in range(len(uncon)):
        a = -10
        while (a<uncon[i]):
            a = random.choice(con)
        matrix[uncon[i]][a] = 1
        con.append(uncon[i])
    try:
        file = open("gen.csv", "w")
        for i in range(nodes):
            file.write("["+str(i)+"]" + ";")
            for j in range(nodes):
                try:
                    if matrix[i][j] != 0:
                        file.write("["+str(j)+"]" + ";")
                except Exception as e:
                    print("can't write to file: ", e)
                    file.close()
            file.write("\n")
        file.close()
    except Exception as e:
        print("can't open file: ", e)
    print("CSV-файл создан")
    print("Проверяем сильносвязность", end="")
    if strong:
        kosadict = {}
        kosadict = csv_to_dict(nodes)
        num = 0
        while len(kosaraju(kosadict)) != 1:
            print(".", end="")
            orient_generate_edges_ves(nodes, 1)
            #print("hell")
        print("[ОК]")
        return matrix

    else:

        return matrix


def norient_generate_edges(nodes): #strong
    uncon =[i for i in range(nodes)]
    con = []
    matrix = np.zeros((nodes, nodes))
    print("Генерируем граф",end="")
    for i in range(nodes):
        if i%20==0:
            print(".", end="")
        for j in range(i + 1, nodes):
            ves = random.randint(0, 1)
            if i != j:
                matrix[i][j] = ves

    for i in range(nodes - 1, 0, -1):
        for j in range(nodes - 1):
            matrix[i][j] = matrix[j][i]
    print("[ОК]")
    print("Проверяем связность", end="")
    for i in range(nodes):
        if i%50==0:
            print(".", end="")
        for j in range (nodes):
            if i != j and matrix[i][j] != 0:
                if len(con)==0:
                    con.append(i)
                    con.append(j)
                    uncon.remove(i)
                    uncon.remove(j)
                a = con.count(i)
                b = con.count(j)
                if a == 0 or b == 0:
                   if a == 0 and b != 0:
                       con.append(i)
                       uncon.remove(i)
                   if b == 0 and a != 0:
                        con.append(j)
                        uncon.remove(j)
    for i in range(nodes-1,0,-1):
        if i%50==0:
            print(".", end="")
        for j in range (nodes):
            if i != j and matrix[i][j] != 0:
                if len(con)==0:
                    con.append(i)
                    con.append(j)
                    uncon.remove(i)
                    uncon.remove(j)
                a = con.count(i)
                b = con.count(j)
                if a == 0 or b == 0:
                   if a == 0 and b != 0:
                       con.append(i)
                       uncon.remove(i)
                   if b == 0 and a != 0:
                        con.append(j)
                        uncon.remove(j)
    con.sort()
    print("[ОК]")
    #print ("unc",uncon)
    #print (con)
    #print(matrix)


    for i in range(len(uncon)):
        a = -10
        while (a<uncon[i]):
            a = random.choice(con)
        matrix[uncon[i]][a] = 1
        con.append(uncon[i])

    #print("unc", uncon)
    #print(con)


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

    #print(matrix)

    return matrix

def orient_generate_edges_ves (nodes, strong):
    uncon = [i for i in range(nodes)]
    con = []
    matrix = np.zeros((nodes, nodes))
    print("Генерируем граф", end="")
    for i in range(nodes):
        if i%20==0:
            print(".", end="")
        for j in range(nodes):
            ves = random.randint(0, 1)
            if i != j and ves == 1:
                matrix[i][j] = random.randint(0, 1000)
    print("[ОК]")
    print("Проверяем связность", end="")
    for i in range(nodes):
        if i%50==0:
            print(".", end="")
        for j in range (nodes):
            if i != j and matrix[i][j] != 0:
                if len(con)==0:
                    con.append(i)
                    con.append(j)
                    uncon.remove(i)
                    uncon.remove(j)
                a = con.count(i)
                b = con.count(j)
                if a == 0 or b == 0:
                   if a == 0 and b != 0:
                       con.append(i)
                       uncon.remove(i)
                   if b == 0 and a != 0:
                        con.append(j)
                        uncon.remove(j)
    for i in range(nodes-1,0,-1):
        if i%50==0:
            print(".", end="")
        for j in range (nodes):
            if i != j and matrix[i][j] != 0:
                if len(con)==0:
                    con.append(i)
                    con.append(j)
                    uncon.remove(i)
                    uncon.remove(j)
                a = con.count(i)
                b = con.count(j)
                if a == 0 or b == 0:
                   if a == 0 and b != 0:
                       con.append(i)
                       uncon.remove(i)
                   if b == 0 and a != 0:
                        con.append(j)
                        uncon.remove(j)
    con.sort()
    print("[ОК]")
    #print ("unc",uncon)
    #print (con)
    #print(matrix)


    for i in range(len(uncon)):
        a = -10
        while (a<uncon[i]):
            a = random.choice(con)
        matrix[uncon[i]][a] = 1
        con.append(uncon[i])

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
    print("Проверяем сильносвязность", end="")
    if strong:

        kosadict = {}
        kosadict = csv_to_dict(nodes)
        num = 0
        while len(kosaraju(kosadict))!=1:
            print(".", end="")
            orient_generate_edges_ves(nodes, 1)
            #print("hell")
        print("[ОК]")
        return matrix

    else:

        return matrix


def norient_generate_edges_ves(nodes): #strong
    uncon = [i for i in range(nodes)]
    con = []
    matrix = np.zeros((nodes, nodes))
    print("Генерируем граф", end="")
    for i in range(nodes):
        if i%20==0:
            print(".", end="")
        for j in range(i + 1, nodes):
            ves = random.randint(0, 1)
            if i != j and ves == 1:
                matrix[i][j] = random.randint(0, 1000)
    for i in range(nodes-1,0, -1):
        for j in range(nodes-1):
            matrix[i][j] = matrix[j][i]
    print("[ОК]")
    print("Проверяем связность", end="")
    for i in range(nodes):
        if i%50==0:
            print(".", end="")
        for j in range (nodes):
            if i != j and matrix[i][j] != 0:
                if len(con)==0:
                    con.append(i)
                    con.append(j)
                    uncon.remove(i)
                    uncon.remove(j)
                a = con.count(i)
                b = con.count(j)
                if a == 0 or b == 0:
                   if a == 0 and b != 0:
                       con.append(i)
                       uncon.remove(i)
                   if b == 0 and a != 0:
                        con.append(j)
                        uncon.remove(j)
    for i in range(nodes-1,0,-1):
        if i%50==0:
            print(".", end="")
        for j in range (nodes):
            if i != j and matrix[i][j] != 0:
                if len(con)==0:
                    con.append(i)
                    con.append(j)
                    uncon.remove(i)
                    uncon.remove(j)
                a = con.count(i)
                b = con.count(j)
                if a == 0 or b == 0:
                   if a == 0 and b != 0:
                       con.append(i)
                       uncon.remove(i)
                   if b == 0 and a != 0:
                        con.append(j)
                        uncon.remove(j)
    con.sort()
    print("[ОК]")
    #print ("unc",uncon)
    #print (con)
    #print(matrix)


    for i in range(len(uncon)):
        a = -10
        while (a<uncon[i]):
            a = random.choice(con)
        matrix[uncon[i]][a] = 1
        con.append(uncon[i])
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
            norient_generate_edges(nodes)
    return nodes

if __name__ == '__main__':
    #test = norient_generate_edges(10)
    #while len(test)<3:
        #test = norient_generate_edges(10)
        #print(len(test))

    generate()