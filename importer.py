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

def csv_to_ves(nodes):
    call = []
    out = []

    file = open("gen.csv", "r")
    kosadict = []
    for i in range(nodes):
        regex = r"[[]\d+[]]"
        test_str = file.readline()
        call.append([])
        out.append([])
        matches = re.finditer(regex, test_str, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            call[i].append(match.group())
            # print(i," "+str(call[i]))

        regex = r"\d+"
        matches = re.finditer(regex, str(call[i]), re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            out[i].append([int(match.group())])

        kosadict.append([])
        for outs in range(1, len(out[i])):
            if out[i][outs] not in kosadict[i]:
                #print("outs ",out[i][outs], "kosa ", kosadict[i] )
                kosadict[i].append(out[i][outs])

        regex = r"([^*[]\d+[^*.\]])"
        call.append([])
        out.append([])
        matches = re.finditer(regex, test_str, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            out[i][matchNum].insert(i,int(match.group()))
            print(kosadict[i])
        for outs in range(1,len(out[i])):
            if out[i][outs] not in kosadict[i]:
                kosadict[i].append(out[i][outs])
                print(i," "+str(kosadict[i]))
    print(kosadict)
    file.close()
    out = []
    print("kosa", len(kosadict))
    for i in range(len(kosadict)):
        #print("len", i, "kosa", len(kosadict))
        print("kosa[]", len(kosadict[i]))
        for j in range(len(kosadict[i])):
            print("sdca",kosadict[i][j])
            out.append([i,kosadict[i][j][0], kosadict[i][j][1]])
        print(out)
    return kosadict

if __name__ == '__main__':
    csv_to_ves(10)