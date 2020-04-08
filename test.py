from lab1 import generate
from importer import csv_to_matrix
def Bfs(G, F, s, t):
    n = len(G)
    queue = []
    queue.append(s)
    global level
    level = n * [0]
    level[s] = 1
    while queue:
        k = queue.pop(0)
        for i in range(n):
            if (F[k][i] < G[k][i]) and (level[i] == 0):
                level[i] = level[k] + 1
                queue.append(i)
    return level[t] != 0


def Dfs(G, F, k, cp):
    tmp = cp
    if k == len(G) - 1:
        return cp
    for i in range(len(G)):
        if (level[i] == level[k] + 1) and (F[k][i] < G[k][i]):
            f = Dfs(G, F, i, min(tmp, G[k][i] - F[k][i]))
            F[k][i] = F[k][i] + f
            F[i][k] = F[i][k] - f
            tmp = tmp - f
    return cp - tmp



def MaxFlow(G, s, t):
    n = len(G)
    F = [n * [0] for i in range(n)]
    flow = 0
    while (Bfs(G, F, s, t)):
        print(".", end="")
        flow = flow + Dfs(G, F, s, 10000000)
    return flow


if __name__ == '__main__':
    print("Сгенерировать новый граф?\n 1 - да\n 0 - нет")
    gen = int(input())
    if gen:
        nodes, G = generate()
    else:
        print("Будет использован граф, находящийся в файле gen.csv")
        input("Нажмите Enter для продолжения...")
        print("ok")
        nodes = 0
        try:
            file = open("gen.csv", "r")
            line = file.readlines()
            nodes = len(line)
            print(nodes)
        except Exception as e:
            print("can't open file: ", e)
        G = csv_to_matrix(nodes)
    file = open("matrix.csv", "w")
    for i in range(nodes):
        file.write(str(G[i])+"\n")
#G = [
#        [0,4,9,0,0,0,0,0],
#        [0,0,0,0,3,4,0,0],
#        [0,0,0,3,2,0,0,0],
#        [0,0,0,0,2,0,0,0],
#        [0,0,0,0,0,0,5,0],
#        [0,0,0,0,0,0,6,2],
#        [0,0,0,4,0,0,0,5],
#        [0,0,0,0,0,0,0,0]
#    ]

    print("Введите точку начала: 0-",nodes-1 )
    source = int(input())  # A
    print("Введите точку конца: 0-", nodes-1)
    sink = int(input())  # F
    max_flow_value = MaxFlow(G, source, sink)
    print("Максимальный поток:", max_flow_value)