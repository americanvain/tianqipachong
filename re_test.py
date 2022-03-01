import re
import json
obj = re.compile(r'"od2":\[(?P<neirong>.*?)\]')
fp =open('./tianqidata.txt','r',encoding='utf-8')
text = fp.read()
result = obj.finditer(text)
for i in result:
    result =i.group("neirong")

obj2 = re.compile(r'{"od21".*?}')
result2 = obj2.finditer(result)
jieguo =''
jieguo_list=[]
for i in result2:
    jieguo =i.group()
    jieguo_list.append(json.loads(jieguo))

tem_list=[]
kongqizhiliang=[]
xiangduishidu=[]
fengli=[]
for i in jieguo_list:
    tem_list.append(i['od22'])
    kongqizhiliang.append(i['od28'])
    xiangduishidu.append(i['od27'])
    fengli.append(str(i['od24'])+str(i['od25'])+'级')


    pass
print(tem_list,kongqizhiliang,xiangduishidu,fengli)
