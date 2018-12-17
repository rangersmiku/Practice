import sys

filename=sys.argv[1]
prefectures=set()

with open(filename) as f:
    line=f.readline()
    while line:
        prefectures.add(line.split()[0])
        line=f.readline()
        
for pref.in prefctures:
    print (pref)
    
    
