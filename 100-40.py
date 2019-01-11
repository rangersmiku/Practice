#coding : utf-8

import Cabocha
import re

fname = 'neko.txt'
fname_parse='neko.txt.cabocha'

def parse_neko():
  
  ''' 「吾輩は猫である」を係り受け解析
    「吾輩は猫である」(neko.txt)を係り受け解析してneko.txt.cabochaに保存する
    '''
    with open(fname) as data_file, open(fname_parsed, mode='w') as out_file:
      
        cabocha=CaboCha.Parser()
        for line in data_file:
            out_file.write(
                cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE)
            )
