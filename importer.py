import re
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")
def csv_to_dict(nodes):
    call=[]
    out = []
    file=open("gen.csv","r")
    kosadict = {}
    for i in range(nodes):
        regex = r"[[]\d+[]]"
        test_str = file.readline()
        call.append([])
        out.append([])
        matches = re.finditer(regex, test_str, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            call[i].append(match.group())
            #print(i," "+str(call[i]))

        regex = r"\d+"
        matches = re.finditer(regex, str(call[i]), re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            out[i].append(int(match.group()))

        kosadict[i] = []
        for outs in range(1,len(out[i])):
            kosadict[i].append(out[i][outs])
    #print(kosadict)
    file.close()
    return kosadict

def csv_to_kruskal(nodes):
    a = []
    nodelist= []
    ves = []
    file = open("gen.csv", "r")
    kosadict = []
    for i in range(nodes):
        regex = r"[[]\d+[]]"
        test_str = file.readline()
        a.append([])
        nodelist.append([])
        ves.append([])
        matches = re.finditer(regex, test_str, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            a[i].append(match.group())
            # print(i," "+str(call[i]))

        regex = r"\d+"
        matches = re.finditer(regex, str(a[i]), re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            nodelist[i].append(int(match.group()))
        nodelist[i].pop(0)
        regex = r"(?<=\*)\d+(?=\*)"
        matches = re.finditer(regex, test_str, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            temp = match.group()
            print("tmp", temp)
            #print("tmp",temp)
            ves[i].append(int(temp))
        for j in range(len(nodelist[i])):
            kosadict.append([i,nodelist[i][j],ves[i][j]])
    #print("out",nodelist)
    #print("ves",ves)
    kosadict.sort(key=sort_key)
    #print("kosa", kosadict)
    file.close()
    out = []
    return kosadict
def csv_to_matrix(nodes):
    matrix = []
    for i in range(nodes):
        matrix.append([])
        for j in range(nodes):
            matrix[i].append(0)
    file = open("gen.csv", "r")
    out=[]
    ves=[]
    for i in range(nodes):
        regex = r"(?<=\[)\d+(?=\])"
        out.append([])
        ves.append([])
        test_str = file.readline()
        matches = re.finditer(regex, test_str, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            out[i].append(int(match.group()))
        out[i].pop(0)
        regex = r"(?<=\*)\d+(?=\*)"
        matches = re.finditer(regex, test_str, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            temp = match.group()
            ves[i].append(int(temp))
    for i in range(nodes):
        k = 0
        for j in range(nodes):
            if j == out[i][k]:
                matrix[i][j]=ves[i][k]
                if k != len(out[i])-1:
                    k+=1
                else:
                    continue
    return matrix

def sort_key(i):
    return i[2]
if __name__ == '__main__':
   mat= csv_to_matrix(50)
   for i in range(50):
       print(mat[i])