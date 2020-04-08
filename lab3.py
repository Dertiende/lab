from lab1 import generate
from importer import csv_to_kruskal

def kruskal():
    way = []
    allves = 0
    nodes,q = generate()
    krulist = csv_to_kruskal(nodes)
    way.append(krulist[0][0])
    way.append(krulist[0][1])
    allves += krulist[0][2]
    list = [krulist[0]]
    while len(way)!=nodes:
        for i in range(len(krulist)):
            if krulist[i][0] in way and krulist[i][1] in way:
                continue
            if krulist[i][0] in way:
                way.append(krulist[i][1])
                allves+=krulist[i][2]
                list.append(krulist[i])
                krulist.remove(krulist[i])
                break
            else:
                if krulist[i][1] in way:
                    way.append(krulist[i][0])
                    allves+=krulist[i][2]
                    list.append(krulist[i])
                    krulist.remove(krulist[i])
                    break
    list.sort()
    for i in range(len(list)):
        list[i][1]=str(list[i][1])+" "+"*"+str(list[i][2])+"*"
        del list[i][2]
    try:
        for i in range(len(list)-1):
            if list[i][0] == list[i+1][0]:
                del list[i+1][0]
                list[i].extend(list[i+1])
                del list [i+1]
    except:
        None
    try:
        file = open("lab3_out.csv", "w")
        for i in range(len(list)):
            for j in range(len(list[i])):
                if j==0:
                    file.write(str("["+str(list[i][j])+"]"+";"))
                else:
                    a = str(list[i][j]).split()
                    a[0]="["+a[0]+"]"
                    s = " ".join(a)
                    file.write(s+";")
            file.write("\n")
        file.close()
    except Exception as e:
        print("can't open file: ", e)
    print("CSV-файл создан")
if __name__ == '__main__':
    kruskal()