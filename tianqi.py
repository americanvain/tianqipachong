#! /usr/bin/env python3
#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import json

def pipei(ori_text):
    obj = re.compile(r'{"od0":"(?P<date>\d+)"')
    date = obj.findall(ori_text)
    date_text=str(date[0])
    fp =open('./tianqidata'+date_text+'.txt','w',encoding='utf-8')
    fp.write(str(date[0])+':\n')

    obj = re.compile(r'"od2":\[(?P<neirong>.*?)\]')
    result = obj.finditer(ori_text)
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
    time_list=[]
    for i in jieguo_list:
        time_list.append(i['od21'])
        tem_list.append(i['od22'])
        kongqizhiliang.append(i['od28'])
        xiangduishidu.append(i['od27'])
        fengli.append(str(i['od24'])+str(i['od25'])+'级')

    for n in range(len(time_list)):
        fp.write(str(time_list[n])+'点整：\n')
        fp.write('温度是:'+str(tem_list[n])+'\n')
        fp.write('空气质量是:'+str(kongqizhiliang[n])+'\n')
        fp.write('相对湿度是:'+str(xiangduishidu[n])+'\n')
        fp.write('风力是:'+str(fengli[n])+'\n')

    pass

if __name__ =="__main__":
    header = {
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'
    }
    url ='http://www.weather.com.cn/weather1d/101280101.shtml'

    html = requests.get(url= url,headers=header)
    html.encoding='utf-8'
    html_text=html.text

    soup = BeautifulSoup(html_text,'lxml')

    tag =soup.find_all('div',class_='left-div')[1]

    pipei(str(tag))
    # fp =open('./tianqidata.txt','w',encoding='utf-8')
    # fp.write(str(tag))
    print("finished")



    pass