import os
import pandas as pd
import numpy as np
import csv

os.chdir('C:/Users/user/Desktop/자료/서울과기대/수업/연구실/개인연구/ntis')
record = pd.read_excel('1.2013(6).xls')

c = record['전담기관 등록(기탁)번호']
count = list(set(c))
print(np.shape(count))

used = []
result = []

for i in range(0, np.shape(record)[0]):
    if record.iloc[i]['전담기관 등록(기탁)번호'] not in used:
        result.append(record.loc[[i]].values.tolist()[0])
        used.append(record.iloc[i]['전담기관 등록(기탁)번호'])

title = ['성과연도', '성과고유번호', '성과구분', '성과명', '전담기관 등록(기탁)번호', '저널명 OR 성과명(영문) 등', '저자 OR 저작자 등', 'IPC OR 등록기관 등', '국내외구분 OR 제조사 등', '초록(국문)', '초록(영문)', '키워드', '유발과제명', '과제고유번호', '부처명', '과제수행기관', '연구수행주체', '6T분류', '과학기술표준분류']
result.insert(0, title)

with open('2.2013(6)-중복제거.csv', 'w', encoding = 'utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(result)
