from dfsbsfs import bfs
from importer import csv_to_dict


def transpose(G):
    P = {}
    for v in G.keys():
        for w in G[v]:
            if w not in P.keys():
                P[w] = [v]
            else:
                P[w].append(v)
    for v in G.keys():
        if v not in P.keys():
            P[v] = []
    return P


def true_dict(D):
    for i in D.keys():
        if D[i] == False:
            return False
    return True


def first_unvisited(D):
    for i in D.keys():
        if D[i] == False:
            return i
    return None


def kosaraju(G):
    stack = []
    visited = {}
    for k in G.keys():
        visited[k] = False
    itera = 0
    while not true_dict(visited):
        if itera % 30 == 0:
            print(".", end="")
        l = first_unvisited(visited)
        c = bfs(G, l)
        c.reverse()

        for i in c:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
        itera += 1
    P = transpose(G)
    ret = []
    for k in G.keys():
        visited[k] = False
    while len(stack) != 0:
        if len(stack) % 30 == 0:
            print(".", end="")
        a = stack.pop()
        if not visited[a]:
            c = bfs(P, a)
            c = list(filter(lambda p: not visited[p], c))
            ret.append(c)
            if c is not None:
                for i in c:
                    visited[i] = True
    return ret


if __name__ == '__main__':
    G = {}
    G = csv_to_dict(10)
    print(G)
    print(len(kosaraju(G)))
