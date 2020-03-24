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

        test_str =file.readline()
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
        regex = r"\d+.0"
        matches = re.finditer(regex, test_str, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            temp = match.group()
            temp = temp[:-2]
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
def sort_key(i):
    return i[2]
if __name__ == '__main__':
    csv_to_kruskal(10)