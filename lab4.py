from lab1 import generate
from dfsbsfs import bfs
from importer import csv_to_dict
def func():
    nodes = generate()
    G = csv_to_dict(nodes)
    vis = []
    komponents = []
    for i in range(nodes):
        if i not in vis:
            visited = (bfs(G,i))
            vis.extend(visited)
            komponents.append(visited)
    max = []
    M = 0
    linelist = []
    for i  in range(len(komponents)):
        if len(komponents[i])> M:
            max = komponents[i]
            M = len(komponents[i])
    try:
        file = open("gen.csv", "r")
        for i in range(nodes):
            linelist.append([file.readline()])
        file.close()
    except Exception as e:
        print("can't open file: ", e)
    file.close()
    try:
        file = open("lab4_out.csv", "w")
        for i in max:
            wr=''.join(linelist[i])
            file.write(wr)
        file.close()
    except Exception as e:
        print("can't open file: ", e)
    print("CSV-файл создан")
    return komponents

if __name__ == '__main__':
    func()