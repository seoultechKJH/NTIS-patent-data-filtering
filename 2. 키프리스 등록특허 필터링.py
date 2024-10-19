### 필요한 모듈
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

os.chdir('C:/Users/user/Desktop/자료/서울과기대/수업/연구실/개인연구/ntis')

info = pd.read_csv('2.2013(6)-중복제거.csv')

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, dump, ElementTree
from bs4 import BeautifulSoup

regispatent = []
for i in range(0, np.shape(info)[0]):
    applinum = info.iloc[i]['전담기관 등록(기탁)번호']
    applinum = re.sub("\-|\/","",str(applinum))
    res = requests.get('http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getBibliographyDetailInfoSearch?applicationNumber='+str(applinum)+'&ServiceKey=BzEOFGerI0flW90Ar02ET5B3t575d2D9T89vnYA4YGo=')
    soup = BeautifulSoup(res.text,'lxml')
    items = soup.find('registerstatus')
    if items != None:
        if items.text == '등록':
            regispatent.append(info.loc[[i]].values.tolist()[0])

    if i == 2999:
        title = ['성과연도', '성과고유번호', '성과구분', '성과명', '전담기관 등록(기탁)번호', '저널명 OR 성과명(영문) 등', '저자 OR 저작자 등', 'IPC OR 등록기관 등', '국내외구분 OR 제조사 등', '초록(국문)', '초록(영문)', '키워드', '유발과제명', '과제고유번호', '부처명', '과제수행기관', '연구수행주체', '6T분류', '과학기술표준분류']
        regispatent.insert(0, title)

        with open('3.2013(6)-등록특허(3000).csv', 'w', encoding = 'utf-8-sig', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(regispatent)
        print('1')
        regispatent = []

    if i == 5999:
        title = ['성과연도', '성과고유번호', '성과구분', '성과명', '전담기관 등록(기탁)번호', '저널명 OR 성과명(영문) 등', '저자 OR 저작자 등', 'IPC OR 등록기관 등', '국내외구분 OR 제조사 등', '초록(국문)', '초록(영문)', '키워드', '유발과제명', '과제고유번호', '부처명', '과제수행기관', '연구수행주체', '6T분류', '과학기술표준분류']
        regispatent.insert(0, title)

        with open('3.2013(6)-등록특허(6000).csv', 'w', encoding = 'utf-8-sig', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(regispatent)
        print('2')
        regispatent = []

    if i == 8999:
        title = ['성과연도', '성과고유번호', '성과구분', '성과명', '전담기관 등록(기탁)번호', '저널명 OR 성과명(영문) 등', '저자 OR 저작자 등', 'IPC OR 등록기관 등', '국내외구분 OR 제조사 등', '초록(국문)', '초록(영문)', '키워드', '유발과제명', '과제고유번호', '부처명', '과제수행기관', '연구수행주체', '6T분류', '과학기술표준분류']
        regispatent.insert(0, title)

        with open('3.2013(6)-등록특허(9000).csv', 'w', encoding = 'utf-8-sig', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(regispatent)
        print('3')
        regispatent = []

    if i == np.shape(info)[0]-1:
        title = ['성과연도', '성과고유번호', '성과구분', '성과명', '전담기관 등록(기탁)번호', '저널명 OR 성과명(영문) 등', '저자 OR 저작자 등', 'IPC OR 등록기관 등', '국내외구분 OR 제조사 등', '초록(국문)', '초록(영문)', '키워드', '유발과제명', '과제고유번호', '부처명', '과제수행기관', '연구수행주체', '6T분류', '과학기술표준분류']
        regispatent.insert(0, title)

        with open('3.2013(6)-등록특허(최종).csv', 'w', encoding = 'utf-8-sig', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(regispatent)
