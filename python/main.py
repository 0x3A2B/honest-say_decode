# -*- coding: utf-8 -*-  
import json
import os

db = {  'oe':'0','oK':'1','ow':'2','oi':'3','7e':'4','7K':'5','7w':'6','7i':'7','Ne':'8','NK':'9' ,'n':'0','6':'1','-':'2','o':'3','v':'4','4':'5','C':'6','S':'7','c':'8','E':'9','z':'0','5':'1','A':'2','i':'3','P':'4','k':'5','s':'6','l':'7','F':'8','q':'9' , 'oc':'2','7z':'7','oz':'3','Nn':'8'};
num = [2,1,1]

def find(input):
   name = input['toNick']
   QQnum = input['fromEncodeUin'][4:]
   massage = input['topicName']
   p = 0
   i = 0
   QQ = ''
   while p<len(QQnum):
      try:
         QQ += db[QQnum[p : p + num[i % 3 ]]]
      except KeyError:
         print("error with %s"%(QQ))
         print("Cantt find %s"%(QQnum[p : p + num[i % 3 ]]))
         break
      p += num[i % 3]
      i+=1
   print("info:%s\tQQ:%s\tname:%s"%(massage,QQ,name))

with open('input.json', 'r',encoding='UTF-8') as f:
    data = json.load(f)
try :
   temp = data['data']['list']
except :
   temp = data['data']['confesses']
for index in temp:
   find(index)
