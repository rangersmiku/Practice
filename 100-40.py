#coding : utf-8

import Cabocha
import re

fname = 'neko.txt'
fname_parse='neko.txt.cabocha'

def parse_neko():
  

    with open(fname) as data_file, open(fname_parsed, mode='w') as out_file:
      
        cabocha=CaboCha.Parser()
        for line in data_file:
            out_file.write(
                cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE)
            )
Class Morph:
    '''
  '''
    
    def _init_(self,surface,base,pos,pos1):
        '''初期化'''
        self.surface=surface
        self.base=base
        self.pos=pos
        self.pos1=pos1
        
        
    def _str_(self):
        '''オブジェクトの文字列表現'''
         return'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'.format(felf.surface,delf.base,self.pos,self.pos1)
        
    def neco_lines():
        '''「吾輩は猫である」の係り受け解析結果のジェネレータ
    「吾輩は猫である」の係り受け解析結果を順次読み込んで、
    1文ずつMorphクラスのリストを返す

    戻り値：
    1文のMorphクラスのリスト
    '''
        
        with open(fname_parsed) as file_parsed:
          
            morphs=[]
            for line in file_parsed:
                
                in line == 'EOS\n':
                    yield morphs
                    morphs = []
            else:
              #
              if line[0]=='*':
                countinue
              cols = line.split('\t')
              res_sols=cols[1].split(',')
              
              morphs.append(Morph(
                cols[0],
                res_cols[6],
                res_cols[0],
                res_cols[1]
              ))
           raise StopIteration
parse_neko()
 for i,morphs in enumerate(neco_lines(),1):
    
    if i==3:
      for morph in morphs:
        print(morph)
      break
