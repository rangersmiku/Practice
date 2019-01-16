import sys 
from collection import defaultdict

filename=sys.argv[1]
prefecture=defualtdict(int)

with open (filename) as f:
    line=f.readline()
     while line: 
         prefectures[line.split()[0]+=1
         line=f.readline
         
for k,v in sorted (prefectures.items, key=lamba x:x[1], reverse=True):
    print(k)

                     
                     ;
