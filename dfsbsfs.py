import sys
from typing import Dict, Any

sys.setrecursionlimit(999999)
def bfs(G, i):
    if i not in G:
        print("Cannot start: graph does not contain vertex ", i)
        return None
    order = []
    visited = [i]
    queue = [i]
    itera = 0
    while len(queue) != 0:
        if itera % 30 == 0:
            print(".", end="")
        v = queue.pop()
        order.append(v)
        al = G[v]
        al = list(filter((lambda a: a not in visited), al))
        visited.extend(al)
        for a in al:
            queue.insert(0, a)
        itera+=1
    return order


def dfs(graph, start,itera, visited):
    #print(itera)
    if itera % 50 == 0:
        print(".", end="")
    visited.append(start)
    temp = graph[start]
    for a in visited:
        if a in temp:
            temp.remove(a)
    for next in temp:
        if next not in visited:
            dfs(graph, next, itera+1, visited)
            itera-=1

    return visited
def dfsstart(vertex,G):
    visited=[]
    n = 0
    dfs(G, vertex, 0, visited)
    for vertex in G:
        if vertex not in visited:
            dfs(G,vertex,0,visited)
            n+=1
    return visited,n

def main():
    G = {0: [1, 4],
         1: [3, 4],
         2: [1],
         3: [4],
         4: [0, 2]}
    # 5: [4],
    # 6: [1, 7, 8],
    # 7: [3, 6],
    # 8: [6]}
    initial = 2
    print(dfsstart(initial, G))
    print (dfs(G,initial,0,visited=[]))
    print(bfs(G,initial))
if __name__ == '__main__':
    main()
