#challenge_0
import sys
import json
jsonfile = sys.argv[1]
f = open(jsonfile)
data = json.load(f)
############################################
dicti={}

if type(data[0])==list:
    column_list=data[0]
    for j in range(0,len(column_list)):
        dicti[column_list[j]]=[]

    for i in range(1,len(data)):
        row_list=data[i]
        for j in range(0,len(row_list)):
            if row_list[j] is None:
                dicti[column_list[j]].append(None)
            else:
                dicti[column_list[j]].append(row_list[j])
if type(data[0])==dict:
    for i in range(0,len(data)):
        for k in data[i].keys():
            dicti[k]=[]
    for i in range(0,len(data)):    
        dict1=data[i] 
        for k in dicti.keys():   
            if k not in dict1.keys():
                dicti[k].append(None)
            else:
                dicti[k].append(dict1[k])
print(dicti)

# Closing file
f.close()