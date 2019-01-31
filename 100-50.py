# coding utf-8
 import re

fname = 'nlp.txt'

def nlp_lines():
    ''' nlp を1文ずつ読み込むジェネレータ
    nlp.txtを順次読み込んで1文ずつ返す

    ’’’
    