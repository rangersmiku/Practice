
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import CaboCha
import pydot

parser = CaboCha.Parser()

sentence = "隣の客はよく柿食う客だ"

tree =  parser.parse(sentence)
cabocha_data = tree.toString(CaboCha.FORMAT_LATTICE)
modify = [] # 1節文の文字列と修飾先の数字を格納
modify_num = -1
section = ""
for line in cabocha_data.splitlines():
    if line == "EOS":
        modify.append([section ,modify_num])
    elif str(line[0]) == "*":
        if section != "":
            modify.append([section ,modify_num])
            section = ""
        modify_num = int(line.split(" ")[2].replace('D', ''))
    else:
        section = section + line.split("\t")[0]

edges = []
for line in modify:
    if line[1] == -1: break
    print( line[0], modify[line[1]][0])
    edges.append([line[0], modify[line[1]][0]])

n = pydot.Node('node')
n.fontname = "arialuni.ttf"
n.fontsize = 9
n.fontcolor = "blue"

g = pydot.graph_from_edges(edges, directed=True)
g.add_node(n)
g.write_png('modify-relation.png', prog='dot')
