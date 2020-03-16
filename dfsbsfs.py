import sys

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
    print("[ОК]")
    return order


def dfs(graph, start,itera, visited = None):
    #print(itera)
    if itera % 50 == 0:
        print(".", end="")
    if visited is None:
        visited = []
    visited.append(start)
    temp = graph[start]
    for a in visited:
        if a in temp:
            temp.remove(a)
    #print("tmp", len(temp))
    #if len(temp) == 0:
        #return visited
    for next in temp:
        if next not in visited:
            dfs(graph, next, itera+1, visited)
            itera-=1
    #visited.reverse()
    #for i  in visited:
        #if visited.count(i)>1:
            #if i % 150 == 0:
                #print(".", end="")
            #visited.remove(i)
    #visited.reverse()
    return visited


def main():
    print(dfs(G, initial))


if __name__ == '__main__':
    G = {0: [1],
         1: [0, 2, 3, 4, 6, 7],
         2: [0, 1, 4],
         3: [1, 7],
         4: [1, 2, 5],
         5: [4],
         6: [1, 7, 8],
         7: [3, 6],
         8: [6]}
    initial = 6
    main()
