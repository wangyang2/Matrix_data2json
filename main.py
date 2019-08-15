import json
import numpy as np
import collections

file=open('CoNLL2009-ST-Chinese-trial.txt','r',encoding='utf-8')
dict1 = collections.OrderedDict()
all_list = []
data_Mat = []  
part_Mat = []
keylist = ['ID','FORM','LEMMA','PLEMMA','POS','PPOS','FEAT','PFEAT','HEAD','PHEAD','DEPREL','PDEPREL','FILLPRED','PRED','APREDS']
for line in file.readlines():
    if line != '\n':
        curLine = line.strip().split("\t")
        part_Mat.append(curLine[:])
    else :
        data_Mat.append(part_Mat)
        part_Mat = []
#print('data_Mat:',data_Mat)

for list1 in data_Mat:
    for list2 in list1:
        for i in range(15):
            if i<14:
                dict1[keylist[i]] = list2[i]
            else :
                dict1[keylist[i]] = list2[i:]
        all_list.append(dict1)
        dict1 = collections.OrderedDict()
#print(all_list)

outputfile=open('result1.json','w',encoding='utf-8')
for index,d in enumerate(all_list):
    if index != len(all_list)-1:
        jsons = json.dumps(d,indent=1,ensure_ascii=False)
        outputfile.write(jsons+','+'\n')
    else :
        jsons = json.dumps(d,indent=1,ensure_ascii=False)
        outputfile.write(jsons)
