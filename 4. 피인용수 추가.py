from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
import os
import pandas as pd
import requests
import json
import numpy as np
import csv
import lxml
import re
import time

os.chdir('C:/Users/김진홍/Desktop/자료/서울과기대/수업/연구실/개인연구/연구/새로운 분석/ntis')

info = pd.read_csv('4.2013(6)-연구정보포함(최종).csv')

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, dump, ElementTree
from bs4 import BeautifulSoup

data = []
count = 0
for i in range(0, np.shape(info)[0]):
    applinum = info.iloc[i]['전담기관 등록(기탁)번호']
    applinum = re.sub("\-|\/","",str(applinum))
    res = requests.get('http://plus.kipris.or.kr/openapi/rest/CitingService/citingInfo?standardCitationApplicationNumber='+str(applinum)+'&accessKey=BzEOFGerI0flW90Ar02ET5B3t575d2D9T89vnYA4YGo=')
    soup = BeautifulSoup(res.text,'lxml')
    a = soup.findAll('citationliteraturetypecodename')
    for j in range(0, len(a)):
        if a[j].text == '발송문서':
            count = count + 1
    
    data.append(info.loc[[i]].values.tolist()[0]+[count])
    count = 0

title = ['성과연도', '성과고유번호', '성과구분', '성과명', '전담기관 등록(기탁)번호', '저널명 OR 성과명(영문) 등', '저자 OR 저작자 등', 'IPC OR 등록기관 등', '국내외구분 OR 제조사 등', '초록(국문)', '초록(영문)', '키워드', '유발과제명', '과제고유번호', '부처명', '과제수행기관', '연구수행주체', '6T분류', '과학기술표준분류', '연구개발단계', '정부연구비', '총연구비', '당해연구시작일', '당해연구종료일', '피인용특허수']
data.insert(0, title)

with open('5.2013(6)-피인용수 추가(최종).csv', 'w', encoding = 'utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
