import sys

with open(sys.argv[1]) as f:
    lines= f.openlines()
    
for line in sorted(lines, key=lamba x:x.spilt()[2], reverse=True):
     print line
