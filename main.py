import codecs
import json
import yindiao_table
from collections import defaultdict
import random

def init(s):
    fuyin=''
    yuanyin=''
    yindiao=-1
    yuan=0
    for ch in s:
        res=yindiao_table.yd.get(ch,(ch,-1))
        if not (-1 in res):
            yuan=1
            yindiao=res[1]
        if not yuan:
            fuyin+=res[0]
        else:
            yuanyin+=res[0]

    return (fuyin,yuanyin,yindiao)

load_list={}  

with codecs.open('word.json','r','utf-8') as f:
    load_list=json.load(f)

pinyin={}
pinyin2=defaultdict(list)

for word in load_list:
    temp=init(word['pinyin'])
    pinyin[word['word']]=temp
    pinyin2[temp].append(word['word'])

while True:
    letter=input('请输入需要押韵的字,输入-1退出: ')
    if letter=='-1':
        break
    py=pinyin.get(letter,(-1,-1,-1))
    if py==(-1,-1,-1):
        print('暂无此字!')

    lis=pinyin2[py]
    print('共查询到%d个字'%(len(lis)))
    for word in range(0,len(lis)):
        ed=','
        if word==len(lis)-1:
            ed='\n'
        print(lis[word],end=ed)
