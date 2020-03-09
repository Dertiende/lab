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

