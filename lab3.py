from lab1 import generate
from importer import csv_to_kruskal

def kruskal():
    way = []
    allves = 0
    nodes = generate()
    krulist = csv_to_kruskal(nodes)
    #print("kru",krulist)
    way.append(krulist[0][0])
    way.append(krulist[0][1])
    allves += krulist[0][2]
    while len(way)!=nodes:
        for i in range(len(krulist)):
            if krulist[i][0] in way and krulist[i][1] in way:
                #print(krulist[i],"цикл",i)
                continue
            if krulist[i][0] in way:
                way.append(krulist[i][1])
                allves+=krulist[i][2]
                #print (i,"i",krulist[i], way, len(krulist),allves)
                krulist.remove(krulist[i])
                break
            else:
                if krulist[i][1] in way:
                    way.append(krulist[i][0])
                    allves+=krulist[i][2]
                    #print(i,"i",krulist[i], way, len(krulist), allves)
                    krulist.remove(krulist[i])
                    break
    print(len(way)," " , way,"  ",allves)
if __name__ == '__main__':
    kruskal()