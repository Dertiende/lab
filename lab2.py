from lab1 import generate
from dfsbsfs import  dfs, bfs
from importer import  csv_to_dict

if __name__ == '__main__':
    nodes = generate()
    G = csv_to_dict(nodes)
    print("Для обхода в ширину введите - 1, в глубину - 0:")
    inp = int(input())
    print("С какой точки начинать обход?")
    tchk = int(input())
    if inp == 1:
        print("Обходим:", end="")
        print(bfs(G, tchk))
    else:
        print("Обходим:", end="")
        D = dfs(G, tchk, 0)
        print("[ОК]")
        print(D)